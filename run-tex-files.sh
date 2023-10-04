#!/bin/bash

# Print a message to indicate that the script is running
echo "Running run-tex-files.sh..."

# Find all .tex files in lectures directory and compile them in their respective directories
find lectures -type f -name "*.tex" -exec sh -c '
  dir="$(dirname "{}")"
  cd "$dir" && pdflatex -interaction=batchmode -halt-on-error "$(basename "{}")"
' \;

# Find all .tex files in homeworks directory and compile them in their respective directories
find homeworks -type f -name "*.tex" -exec sh -c '
  dir="$(dirname "{}")"
  cd "$dir" && pdflatex -interaction=batchmode -halt-on-error "$(basename "{}")"
' \;

# Run python file to compile combined pdfs
python3 ./pdf_merger.py