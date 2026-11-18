"""Chapter 01: call pretrained model weights directly."""

import argparse
import os

import torch
from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer, FineGrainedFP8Config


def load_model():
    name = os.getenv("LLM_MODEL", "Qwen/Qwen3-4B-Instruct-2507")
    config = AutoConfig.from_pretrained(name)
    options = {"device_map": "auto", "dtype": "auto"}
    if getattr(config, "quantization_config", {}).get("quant_method") == "fp8":
        options["quantization_config"] = FineGrainedFP8Config(dequantize=True)
    tokenizer = AutoTokenizer.from_pretrained(name)
    model = AutoModelForCausalLM.from_pretrained(name, **options).eval()
    return tokenizer, model


def call_model(messages):
    global _loaded
    if _loaded is None:
        _loaded = load_model()
    tokenizer, model = _loaded
    text = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True, enable_thinking=False
    )
    inputs = tokenizer(text, return_tensors="pt").to(model.device)
    with torch.inference_mode():
        output = model.generate(**inputs, max_new_tokens=128, do_sample=False)
    tokens = output[0, inputs["input_ids"].shape[1]:]
    return {"role": "assistant", "content": tokenizer.decode(tokens, skip_special_tokens=True)}


_loaded = None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prompt", nargs="?", default="Say exactly: Hello World!!!")
    args = parser.parse_args()
    messages = [{"role": "user", "content": args.prompt}]
    reply = call_model(messages)
    print(reply["content"])


if __name__ == "__main__":
    main()
