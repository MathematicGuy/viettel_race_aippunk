import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, pipeline
from langchain_huggingface import HuggingFacePipeline


def load_llm():
    MODEL_PATH = "Qwen/Qwen2.5-3B-Instruct"  # Local model path

    # ✅ Optimized 4-bit quantization config for Blackwell GPUs
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,     # Nested quantization → less VRAM
        bnb_4bit_quant_type="nf4",          # Best quantization format for LLMs
        bnb_4bit_compute_dtype=torch.bfloat16,  # BF16 is optimal on Blackwell
    )

    # ✅ Load tokenizer & model locally with full GPU optimization
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        quantization_config=bnb_config,
        device_map="auto",                  # Automatically spreads across GPUs if available
        dtype=torch.bfloat16,         # Native dtype for new NVIDIA architectures
        local_files_only=True,
    )

    # ✅ Enable better CUDA performance
    torch.backends.cuda.matmul.allow_tf32 = True     # TensorFloat-32 acceleration
    torch.backends.cudnn.benchmark = True            # Optimize kernel selection
    torch.set_float32_matmul_precision("high")       # Prefer high precision kernels

    # ✅ Create high-throughput inference pipeline
    generation_pipeline = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=256,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.1,
    )

    return HuggingFacePipeline(pipeline=generation_pipeline)