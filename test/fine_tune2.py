# Cell 2: Imports và cấu hình chung
import os, json, base64
from pathlib import Path
from pdf2image import convert_from_path
import traceback

import torch
from datasets import load_dataset
from transformers import (
    AutoProcessor,
    Qwen2VLForConditionalGeneration,
    Trainer,
    TrainingArguments,
    DataCollatorForSeq2Seq,
)
from peft import LoraConfig, get_peft_model

# Thư mục dữ liệu
PDF_DIR      = Path("training2/training_input")     # chứa *.pdf
MD_DIR       = Path("training2/training_output")       # mỗi subfolder chứa main.md
PAGE_IMG_DIR = Path("pages")              # lưu ảnh full-page
TRAIN_JSON   = "train.json"

# Model & training config
MODEL_NAME   = "opendatalab/MinerU2.5-2509-1.2B"
BATCH_SIZE   = 2
ACCUM_STEPS  = 8
EPOCHS       = 3
LR           = 1e-4

PAGE_IMG_DIR.mkdir(exist_ok=True)


raw_ds = load_dataset("json", data_files=TRAIN_JSON, split="train")
processor = AutoProcessor.from_pretrained(MODEL_NAME)
tokenizer = processor.tokenizer


# Cell 4: Windows-compatible multiprocessing version
def preprocess_fn_batched(batch, model_name="opendatalab/MinerU2.5-2509-1.2B"):
    """Process multiple samples at once - Windows multiprocessing compatible"""
    import base64
    from transformers import AutoProcessor  # ✅ Import inside function

    # ✅ Load processor inside function (each worker gets its own copy)
    processor = AutoProcessor.from_pretrained(model_name)
    tokenizer = processor.tokenizer

    batch_size = len(batch["conversations"])

    input_ids_list = []
    attention_mask_list = []
    pixel_values_list = []
    labels_list = []

    for i in range(batch_size):
        user = batch["conversations"][i][0]
        assistant_b64 = batch["conversations"][i][1]["content_base64"]

        assistant_text = base64.b64decode(assistant_b64).decode("utf-8")
        prompt = user["content"][-1]["text"]
        img_list = [c["image"] for c in user["content"] if c["type"]=="image"]

        inputs = processor(
            text=[prompt],
            images=img_list,
            padding=True,
            return_tensors="pt"
        )

        labels = tokenizer(
            assistant_text,
            return_tensors="pt",
            add_special_tokens=False
        ).input_ids

        # In preprocess_fn_batched, before appending
        if inputs.pixel_values is None:
            raise ValueError(f"Pixel values are None for sample {i}")

        print(f"Pixel values shape: {inputs.pixel_values.shape}")
        traceback.print_exc()

        input_ids_list.append(inputs.input_ids[0])
        attention_mask_list.append(inputs.attention_mask[0])
        pixel_values_list.append(inputs.pixel_values[0])
        labels_list.append(labels[0])

    return {
        "input_ids": input_ids_list,
        "attention_mask": attention_mask_list,
        "pixel_values": pixel_values_list,
        "labels": labels_list,
    }

# Now multiprocessing will work!
ds = raw_ds.map(
    preprocess_fn_batched,
    batched=True,
    batch_size=5,
    remove_columns=["conversations"],
    num_proc=7,
    load_from_cache_file=True,
    desc="Processing samples",
    fn_kwargs={"model_name": MODEL_NAME}
)


device = "mps" if torch.backends.mps.is_available() else "cuda" if torch.cuda.is_available() else "cpu"
print(device)


# Cell 5: Load model và cấu hình LoRA
model = Qwen2VLForConditionalGeneration.from_pretrained(
    MODEL_NAME,
    trust_remote_code=True,
    device_map="auto",
    dtype=torch.bfloat16
)

lora_cfg = LoraConfig(
    task_type="CAUSAL_LM",
    inference_mode=False,
    r=32,
    lora_alpha=16,
    lora_dropout=0.05,
    target_modules=[
        "q_proj","k_proj","v_proj","o_proj",
        "gate_proj","up_proj","down_proj"
    ]
)
model = get_peft_model(model, lora_cfg)


# Cell 6: Cấu hình Trainer
# data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, padding=True)

# # Cell 6: Training configuration
# training_args = TrainingArguments(
#     output_dir="mineru_lora_finetuned",

#     # GPU parameters (independent of CPU)
#     per_device_train_batch_size=2,    # ← Based on GPU VRAM
#     gradient_accumulation_steps=8,     # ← Effective batch = 16

#     # CPU-related (data loading)
#     dataloader_num_workers=4,          # ← 4 workers for data loading
#     # ↑ Separate from preprocessing num_proc

#     learning_rate=LR,
#     num_train_epochs=EPOCHS,
#     bf16=True,                         # ← Better than fp16 for your model
#     save_steps=200,
#     save_total_limit=2,
#     logging_steps=20,
#     remove_unused_columns=False,
#     report_to="none"
# )

# trainer = Trainer(
#     model=model,
#     args=training_args,
#     train_dataset=ds,
#     data_collator=data_collator,
#     processing_class=tokenizer
# )