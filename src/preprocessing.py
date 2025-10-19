import os
import logging
from io import BytesIO
from pathlib import Path
import subprocess

import docling
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.backend.pypdfium2_backend import PyPdfiumDocumentBackend
from docling.pipeline.standard_pdf_pipeline import StandardPdfPipeline


from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.datamodel.base_models import InputFormat
from docling_core.types.io import DocumentStream
from docling.datamodel.pipeline_options import TableFormerMode
from docling.datamodel.accelerator_options import AcceleratorDevice, AcceleratorOptions
from docling.datamodel.document import ConversionResult
from docling.datamodel.pipeline_options_vlm_model import ApiVlmOptions, ResponseFormat
from docling.datamodel.pipeline_options import (
    VlmPipelineOptions,
)
from docling.pipeline.vlm_pipeline import VlmPipeline

from PIL import Image
import torch
from transformers import AutoTokenizer, AutoProcessor, AutoModelForImageTextToText, BitsAndBytesConfig
import time
import socket

# Step 1 — Set env vars before starting server
os.environ["OLLAMA_FLASH_ATTENTION"] = "true"
os.environ["OLLAMA_LOW_VRAM"] = "false"
os.environ["OLLAMA_NUM_PARALLEL"] = "4"
os.environ["OLLAMA_CONTEXT_LENGTH"] = "2048"

# Step 2 — Start Ollama server with these variables

def is_ollama_running():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex(('localhost', 11434))
	sock.close()
	return result == 0

if not is_ollama_running():
	ollama_proc = subprocess.Popen(["ollama", "serve"], env=os.environ)
	time.sleep(5)  # wait for Ollama to be ready
else:
	print("Ollama is already running")


# MODEL_PATH = "benhaotang/Nanonets-OCR-s:latest"  # local HF model
MODEL_PATH = "benhaotang/Nanonets-OCR-s:q4_k_m"
os.environ['TRANSFORMERS_VERBOSITY'] = 'info'


def create_vlm_options(model:str, prompt:str):
    options = ApiVlmOptions(
        url="http://localhost:11434/v1/chat/completions",  # the default Ollama endpoint # type: ignore
        params=dict(
            model=model,
        ),
        prompt=prompt,
        timeout=350,
        scale=1.0,
        response_format=ResponseFormat.MARKDOWN,
    )

    return options


# ===========================
# 2️⃣ Configure Docling
# ===========================
def doc_converter():
    logging.basicConfig(level=logging.INFO)
    system_prompt = """
        Hãy trích xuất toàn bộ văn bản từ tài liệu ở trên giống như cách bạn đọc nó một cách tự nhiên.
        Trả về các bảng dưới dạng mã HTML.
        Trả về các phương trình dưới dạng biểu diễn LaTeX.

        Nếu trong tài liệu có hình ảnh nhưng không có chú thích, hãy thêm một mô tả ngắn cho hình ảnh đó bên trong thẻ <img></img>;
        nếu hình ảnh đã có chú thích, hãy đặt chú thích đó bên trong thẻ <img></img>.

        Dấu watermark nên được đặt trong thẻ <watermark></watermark>.
        Số trang nên được đặt trong thẻ <page_number></page_number>.
        Ví dụ: <page_number>14</page_number> hoặc <page_number>9/22</page_number>.

        Ưu tiên sử dụng ký hiệu ☐ và ☑ cho các ô kiểm (checkbox).

        QUAN TRỌNG: Luôn luôn trả lời bằng **Tiếng Việt**.
    """

    #? run remote Ollama, Huggingface model
    pdf_options = VlmPipelineOptions(
        enable_remote_services=True  # required when calling remote VLM endpoints
    )
    pdf_options.accelerator_options = AcceleratorOptions(
        num_threads=12, device=AcceleratorDevice.AUTO
    )
    pdf_options.vlm_options = create_vlm_options(
        model=MODEL_PATH,
        prompt=system_prompt,
    )

    converter = DocumentConverter(
        # allowed_formats=[
        #     InputFormat.PDF,
        #     InputFormat.IMAGE,
        #     InputFormat.DOCX,
        #     InputFormat.HTML,
        #     InputFormat.PPTX,
        # ],  # whitelist formats, non-matching files are igno

        format_options={
            InputFormat.PDF: PdfFormatOption(
                pipeline_options=pdf_options,
                pipeline_cls=VlmPipeline,
            )
        }
    )

    return converter


# ===========================
# 3️⃣ Main PDF → Markdown pipeline
# ===========================
def extract_text_to_markdown(input_dir: str, output_dir: str):
    output_dir = Path('scratch') # type: ignore
    output_dir.mkdir(parents=True, exist_ok=True) # type: ignore

    data_folder = Path(__file__).parent / input_dir # get absoluate path, inefficient but get the job done.
    file_names = os.listdir(data_folder)
    file_list = [data_folder/file_name for file_name in file_names]


    # process_mul_files_example = [
    #     "tests/data/html/wiki_duck.html",
    #     "tests/data/docx/word_sample.docx",
    #     "tests/data/docx/lorem_ipsum.docx",
    #     "tests/data/pptx/powerpoint_sample.pptx",
    #     "tests/data/2305.03393v1-pg9-img.png",
    #     "tests/data/pdf/2206.01062.pdf",
    # ]

    converter = doc_converter() # DocumentConverter()
    conv_results_iter = converter.convert_all(file_list) # extract multiple files
    docs = [result.document for result in conv_results_iter]

    # with open(file_path, "rb") as f:
    #     body_stream = BytesIO(f.read())

    for file_name, doc in zip(file_names, docs):
        with open(f"{output_dir}/{file_name[:-4]}.md", "w", encoding='utf-8') as f:
            f.write(doc.export_to_markdown())

    # ollama_proc.terminate() # AUTO turn off Ollama
    # return markdown_outs

if __name__ == '__main__':
    start_time = time.perf_counter()  # Use perf_counter for higher precision
    extract_text_to_markdown('private-test-input', 'scratch')

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.4f} seconds")
    ollama_proc.terminate() # type: ignore