import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, pipeline
from langchain_huggingface import HuggingFacePipeline
import os
from huggingface_hub import HfApi

def validate_hf_token():
    token = os.getenv("HF_TOKEN")
    if not token:
        raise ValueError("Hugging Face token is not set. Please set the HF_TOKEN environment variable.")
    try:
        api = HfApi(token=token)
        api.whoami()  # Validates the token
        print("Hugging Face token is valid.")
    except Exception as e:
        raise ValueError(f"Invalid Hugging Face token: {e}")

def load_llm():
    validate_hf_token()
    # MODEL_PATH = "Qwen/Qwen2.5-3B-Instruct"
    MODEL_PATH = "google/gemma-3-1b-it"
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,     # Nested quantization → less VRAM
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
    )

    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        quantization_config=bnb_config,
        device_map="auto",
        dtype=torch.bfloat16,         # Native dtype for new NVIDIA architectures
        local_files_only=True,
    )

    # Enable better CUDA performance
    torch.backends.cuda.matmul.allow_tf32 = True     # TensorFloat-32 acceleration
    torch.backends.cudnn.benchmark = True            # Optimize kernel selection
    torch.set_float32_matmul_precision("high")       # Prefer high precision kernels

    # Create high-throughput inference pipeline
    generation_pipeline = pipeline(
        "question-answering",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=256,
        temperature=0.4,
        top_p=0.8,
        repetition_penalty=1.1,
    )

    return HuggingFacePipeline(pipeline=generation_pipeline)


if __name__ == "__main__":
    # Use a pipeline as a high-level helper
	from transformers import pipeline

	validate_hf_token()
	pipe = pipeline("text-generation", model="google/gemma-3-1b-it")
	messages = [
		{"role": "user", "content": "Who are you?"},
	]
	pipe(messages)
