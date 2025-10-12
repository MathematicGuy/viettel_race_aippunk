import re
import subprocess
import os, shutil, sys

#? Config MinerU
PATH = "private_test_input/"
OUTPUT_PATH = "private_test_output"
MAX_WORKERS = 4  # Adjust based on your VRAM and CPU

# ==== Device & Precision ====
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
os.environ["MINERU_USE_GPU"] = "True"
os.environ["MINERU_DEVICE"] = "cuda"
os.environ["MINERU_USE_FP16"] = "True"
os.environ["MINERU_MAX_GPU_MEMORY"] = "16G"  # for your 16GB VRAM
os.environ["MINERU_ENABLE_PARALLEL"] = "true"  # process multiple pages at once

# ==== Batch & Memory Control ====
os.environ["MINERU_BATCH_SIZE"] = "8"
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:128"

# ==== Disable Visualization ====
os.environ["MINERU_SAVE_VISUALIZATION"] = "False"
os.environ["MINERU_SAVE_INTERMEDIATE"] = "False"


for key in [
    "MINERU_DEVICE",
    "MINERU_USE_GPU",
    "MINERU_USE_FP16",
    "MINERU_SAVE_VISUALIZATION",
    'MINERU_SAVE_INTERMEDIATE',
    'MINERU_MAX_GPU_MEMORY',
]:
    print(f"{key} = {os.getenv(key)}")


def process_pdf(file_name):
    input_path = os.path.join(PATH, file_name)
    result = subprocess.run([
        "mineru",
        "-p", input_path,
        "-o", OUTPUT_PATH,
        "--disable-visualization",
        "--disable-intermediate"
    ], capture_output=True, text=True)

    if result.returncode == 0:
        return f"✅ Success: {file_name}"
    else:
        return f"❌ Failed: {file_name}\n{result.stderr}"


# Run in parallel
from concurrent.futures import ThreadPoolExecutor, as_completed

file_names = [f for f in os.listdir(PATH) if f.lower().endswith(".pdf")]

with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    futures = [executor.submit(process_pdf, f) for f in file_names]
    for future in as_completed(futures):
        print(future.result())

file_names = os.listdir(PATH) # [file_name.pdf,...]

for file_name in file_names:
    file_name = file_name.replace('.pdf', '')
    file_path = f'private_test_output/{file_name}/auto/'

    with open(f'{file_path}/{file_name}.md', 'r', encoding='utf-8') as f:
        content = f.read()

    cleaned = re.sub(r"<table>.*?VIETTEL AI RACE.*?</table>", "", content, flags=re.S | re.I)
    with open(f'{file_path}/clean_{file_name}.md', 'w', encoding='utf-8') as f:
        f.write(cleaned)