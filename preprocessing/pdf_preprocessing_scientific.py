import os
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

import torch

print("BEGIN PDF PREPROCESSING: CONVERT PDF to MARKDOWN using NOUGAT")

# ==== Paths ====
PATH = "private-test-input/"
OUTPUT_PATH = "private-test-output/"
os.makedirs(OUTPUT_PATH, exist_ok=True)

MAX_WORKERS = 8  # Adjust based on GPU memory and PDF size

# ==== Device Settings ====
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
os.environ["NO_ALBUMENTATIONS_UPDATE"] = "1"
DEVICE = "cuda"  # or "cpu" if no GPU
BATCH_SIZE = "4"
print('cuda available:', torch.cuda.is_available())

# ==== Function to process PDF using NOUGAT ====
def process_pdf(file_name):
    input_path = os.path.join(PATH, file_name)
    output_file = os.path.join(OUTPUT_PATH, file_name.replace(".pdf", ".mmd"))

    result = subprocess.run([
        "nougat",
        input_path,
        "--out", output_file,
        "--batchsize", BATCH_SIZE
        "--markdown"
    ], capture_output=True, text=True)

    if result.returncode == 0:
        return f"✅ Success: {file_name}"
    else:
        return f"❌ Failed: {file_name}\n{result.stderr}"


# ==== Parallel Processing ====
file_names = [f for f in os.listdir(PATH) if f.lower().endswith(".pdf")]
print(f"Found {len(file_names)} PDFs:", file_names)

with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    futures = [executor.submit(process_pdf, f) for f in file_names]
    for future in as_completed(futures):
        print(future.result())
        print()


# ==== Postprocess: Clean unwanted tables ====
for file_name in file_names:
    base_name = file_name.replace(".pdf", "")
    md_path = os.path.join(OUTPUT_PATH, f"{base_name}.mmd")

    if not os.path.exists(md_path):
        print(f"⚠️ File not found: {md_path}")
        continue

    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    cleaned = re.sub(r"<table>.*?VIETTEL AI RACE.*?</table>", "", content, flags=re.S | re.I)

    clean_path = os.path.join(OUTPUT_PATH, f"clean_{base_name}.mmd")
    with open(clean_path, "w", encoding="utf-8") as f:
        f.write(cleaned)

    print(f"🧹 Cleaned and saved: {clean_path}")
