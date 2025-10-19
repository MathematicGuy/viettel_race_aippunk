#!/bin/bash

set -e

# Convert pdf -> .md using MinerU
python preprocessing/pdf_preprocessing.py

# remove redundant file leaving only images/ and file.md
python preprocessing/reorganize_directories.py

# remove watermark images and rename useful images
python preprocessing/rename_images.py

# clearn markdown
python preprocessing/clean_markdown.py

# save all data from private-test-output to Milvus vectordb
python preprocessing/save_to_milvus.py
