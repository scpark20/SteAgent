"""Exercise device selection without requiring model weights or a GPU."""

import importlib.util
import os
from pathlib import Path
import unittest
from unittest.mock import MagicMock, patch


class ModelDeviceTests(unittest.TestCase):
    def load(self, mps_available, device=None):
        torch = MagicMock()
        torch.backends.mps.is_available.return_value = mps_available
        transformers = MagicMock()
        transformers.AutoConfig.from_pretrained.return_value.quantization_config = {}
        environment = {"LLM_MODEL": "example/checkpoint"}
        if device is not None:
            environment["LLM_DEVICE"] = device
        path = Path(__file__).resolve().parents[1] / "code/chapter-01/agent.py"
        spec = importlib.util.spec_from_file_location("device_test_chapter", path)
        module = importlib.util.module_from_spec(spec)
        with patch.dict("sys.modules", {"torch": torch, "transformers": transformers}):
            with patch.dict(os.environ, environment, clear=True):
                spec.loader.exec_module(module)
                module.load_model()
        return transformers.AutoModelForCausalLM.from_pretrained.call_args.kwargs, torch

    def test_apple_gpu_uses_mps_with_half_precision(self):
        options, torch = self.load(mps_available=True)
        self.assertEqual(options["device_map"], "mps")
        self.assertIs(options["dtype"], torch.float16)

    def test_non_mps_hosts_keep_automatic_device_mapping(self):
        options, _ = self.load(mps_available=False)
        self.assertEqual(options, {"device_map": "auto", "dtype": "auto"})

    def test_explicit_cpu_overrides_available_apple_gpu(self):
        options, _ = self.load(mps_available=True, device="cpu")
        self.assertEqual(options, {"device_map": "cpu", "dtype": "auto"})


if __name__ == "__main__":
    unittest.main()
