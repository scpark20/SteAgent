import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch


def chapter(number):
    path = Path(__file__).resolve().parents[1] / f"code/chapter-{number:02}/agent.py"
    spec = importlib.util.spec_from_file_location(f"chapter_{number}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def request(a=12, b=30, name="add"):
    return {"role": "assistant", "content": "", "tool_calls": [
        {"function": {"name": name, "arguments": {"a": a, "b": b}}}
    ]}


class AgentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.agent = chapter(8)

    def invoke(self, replies, max_steps=8):
        with patch.object(self.agent, "call_model", side_effect=replies) as model:
            state = self.agent.build_graph(max_steps).invoke(
                {"messages": [{"role": "user", "content": "Test"}], "calls": 0})
        return state, model

    def test_greeting_needs_no_tool(self):
        state, model = self.invoke([{"role": "assistant", "content": "Hello World!!!"}])
        self.assertEqual(state["calls"], 1)
        self.assertEqual(model.call_count, 1)
        self.assertEqual([m["role"] for m in state["messages"]], ["user", "assistant"])

    def test_tool_result_reaches_the_next_model_call(self):
        state, model = self.invoke([request(), {"role": "assistant", "content": "42"}])
        observation = model.call_args_list[1].args[0][-1]
        self.assertEqual(observation["role"], "tool")
        self.assertEqual(json.loads(observation["content"]), {"result": 42})
        self.assertEqual(state["messages"][-1]["content"], "42")

    def test_multiple_rounds_keep_all_observations(self):
        state, model = self.invoke([request(1, 2), request(3, 4), {"role": "assistant", "content": "7"}])
        results = [json.loads(m["content"]) for m in state["messages"] if m["role"] == "tool"]
        self.assertEqual(results, [{"result": 3}, {"result": 7}])
        self.assertEqual(model.call_count, 3)

    def test_invalid_tool_request_is_returned_to_model(self):
        state, model = self.invoke([request(name="missing"), {"role": "assistant", "content": "Cannot use that tool."}])
        observation = model.call_args_list[1].args[0][-1]
        self.assertIn("Unknown tool", json.loads(observation["content"])["error"])
        self.assertEqual(state["calls"], 2)

    def test_invalid_arguments_do_not_execute_as_valid_numbers(self):
        for value in ["12", True, float("inf"), float("nan"), None]:
            with self.subTest(value=value):
                result = self.agent.execute_tool(request(value)["tool_calls"][0])
                self.assertIn("error", json.loads(result["content"]))

    def test_tool_runtime_failure_becomes_an_observation(self):
        def fail(**kwargs):
            raise RuntimeError("Example failure")
        with patch.dict(self.agent.REGISTRY, {"add": fail}):
            result = self.agent.execute_tool(request()["tool_calls"][0])
        self.assertEqual(json.loads(result["content"]), {"error": "Example failure"})

    def test_step_limit_stops_before_another_action(self):
        with patch.object(self.agent, "call_model", return_value=request()) as model:
            with patch.object(self.agent, "execute_tool") as executor:
                with self.assertRaisesRegex(RuntimeError, "Step limit"):
                    self.agent.build_graph(1).invoke({"messages": [], "calls": 0})
                executor.assert_not_called()
            self.assertEqual(model.call_count, 1)

    def test_final_answer_is_allowed_at_limit(self):
        state, _ = self.invoke([{"role": "assistant", "content": "Done"}], max_steps=1)
        self.assertEqual(state["messages"][-1]["content"], "Done")

    def test_invalid_budget_is_rejected(self):
        with self.assertRaises(ValueError):
            self.agent.build_graph(0)

    def test_chapter_six_stops_at_tool_result_and_seven_closes_loop(self):
        for number, expected_calls, expected_role in [(6, 1, "tool"), (7, 2, "assistant")]:
            with self.subTest(chapter=number):
                module = chapter(number)
                with patch.object(module, "call_model", side_effect=[request(), {"role": "assistant", "content": "42"}]) as model:
                    state = module.build_graph().invoke({"messages": []})
                self.assertEqual(model.call_count, expected_calls)
                self.assertEqual(state["messages"][-1]["role"], expected_role)


if __name__ == "__main__":
    unittest.main()
