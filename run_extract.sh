#!/bin/bash

# Run the main Python script
python pdf_preprocessing.py

python reorganize_directories.py

python rename_images.py