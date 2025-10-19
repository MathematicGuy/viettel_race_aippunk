## Hướng dẫn cài thư viện cho Preprocessing
```sh
pip install -r requirements.txt
```


## Hướng dẫn cài Docker cho Milvus (Chú Ý: Conflict nếu có 1 Milvusdb standalone đã khơi tạo khác, tránh sử dụng 1 MilvusDB khác trong Docker)
0. Download [Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/)

Rồi Chạy trong Terminal:
**Windows (Powershell):**
1. Open Docker Desktop in administrator mode by right-clicking and selecting Run as administrator.
2. Download the installation script and save it as standalone.bat.
```sh
Invoke-WebRequest https://raw.githubusercontent.com/milvus-io/milvus/refs/heads/master/scripts/standalone_embed.bat -OutFile standalone.bat
```
3. Run the downloaded script to start Milvus as a Docker container.
```sh
standalone.bat start
```


**Linux (Linux or Windows GitBash):**
1. Download the installation script
```sh
curl -sfL https://raw.githubusercontent.com/milvus-io/milvus/master/scripts/standalone_embed.sh -o standalone_embed.sh
```
2. Start the Docker container
```sh
bash standalone_embed.sh start
```

## Hướng dẫn cài thư viện cho dự đoán câu hỏi (tải cuda và flash hỗ trợ GPU kiến trúc Blackwell)
```sh
cd flash-installation
pip install -r requirements.txt
cd ..
```


## Directory Structure
```
app/
├── main.py                    # Main entry point
├── requirements.txt           # Python dependencies
├── *.sh                       # Shell scripts (run_chooser_answer.sh, run_extract.sh, standalone_embed.sh)
│
├── config/                    # Configuration files
│   ├── user.yaml
│   ├── embedEtcd.yaml
│   └── zilliz-cloud-Free-01-username-password.txt
│
├── core/                      # Core pipeline functionality
│   ├── __init__.py
│   └── pipeline.py           # Hybrid search pipeline creation
│
├── models/                    # ML models and encoders
│   ├── __init__.py
│   ├── llm_utils.py          # LLM loading and configuration
│   └── image_encoder.py      # CLIP-based image encoder
│
├── processors/                # Data processors
│   ├── __init__.py
│   ├── markdown_processor.py # Markdown extraction
│   └── entity_processors.py  # Text and image entity processing
│
├── preprocessing/             # PDF and file preprocessing
│   ├── __init__.py
│   ├── pdf_preprocessing.py
│   ├── rename_images.py
│   └── reorganize_directories.py
│
├── retrieval/                 # Search and retrieval components
│   ├── __init__.py
│   ├── search_engine.py      # Hybrid search engine
│   └── retrieval_qa.py       # QA retrieval and prompts
│
├── storage/                   # Vector database storage
│   ├── __init__.py
│   └── milvus_store.py       # Milvus hybrid store
│
├── utils/                     # Utility functions
│   ├── __init__.py
│   └── combine_markdown.py   # Markdown combination utilities
│
└── data/                      # Data files
    ├── answer_task_qa.csv
    ├── question.csv
    ├── validate_data.py
    └── validate_task_qa.csv
```

## Module Descriptions

### `config/`
Contains all configuration files including YAML configs and credentials.

### `core/`
Contains the main pipeline logic that orchestrates the entire hybrid search workflow.

### `models/`
Manages ML models:
- **llm_utils.py**: LLM loading with quantization for efficient inference
- **image_encoder.py**: CLIP-based multimodal image and text encoding

### `processors/`
Data processing modules:
- **markdown_processor.py**: Extracts text, tables, and images from markdown files
- **entity_processors.py**: Creates text and image entities for embedding

### `preprocessing/`
PDF and file preprocessing utilities for data preparation.

### `retrieval/`
Search and QA components:
- **search_engine.py**: Hybrid search combining dense, sparse, and multimodal vectors
- **retrieval_qa.py**: Document retrieval and MCQ prompting

### `storage/`
Vector database integration:
- **milvus_store.py**: Milvus collection creation and entity insertion

### `utils/`
General utility functions for tasks like markdown file combination.


## Milvus GUI
Run this in web: `http://127.0.0.1:9091/webui/` where 'http://127.0.0.1' is your local host address with 9091 as Milvus GUI default port.


### Export ENV KEY
"""
Debugging FastAPI:
uvicorn app.py:app --reload

MacOS:
export TOGETHER_API_KEY="YOUR_API_KEY"

Windows:
$env:CEREBRAS_API_KEY = "your_key"
$env:QDRANT_URL = "your_url"
$env:QDRANT_API_KEY = "your_key"
"""