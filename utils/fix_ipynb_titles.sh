#!/bin/bash

# Function to fix notebook first title
fix_notebook_formatting() {
  local file=$1
  if [ -f "$file" ]; then
    jq '.cells[0].source |= .[2:]' "$file" > tmp.ipynb && mv tmp.ipynb "$file"
  else
    echo "File not found: $file"
  fi
}

if [ $# -gt 0 ]; then
  # If a single path is provided as an argument, fix this one
  fix_notebook_formatting "$1"
else
  # Else, iterate over each file listed in QUARTO_PROJECT_OUTPUT_FILES
  if [ -z "$QUARTO_PROJECT_OUTPUT_FILES" ]; then
    echo "QUARTO_PROJECT_OUTPUT_FILES environment variable is not set."
    exit 1
  fi
  while IFS= read -r file; do
    fix_notebook_formatting "$file"
  done <<< "$QUARTO_PROJECT_OUTPUT_FILES"
fi
