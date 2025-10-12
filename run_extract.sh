#!/bin/bash

# Run the main Python script
python preprocessing.pdf_preprocessing.py

python preprocessing.reorganize_directories.py

python preprocessing.rename_images.py