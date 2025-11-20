#!/bin/bash

LANGUAGE=$1
SECTION=$2
CHAPTER=$3

WORK_DIR=/home/onyxia/work
CLONE_DIR=${WORK_DIR}/repo-git
CHAPTER_DIR=${CLONE_DIR}/source/${SECTION}/${CHAPTER}

# Clone course repository
REPO_URL=https://github.com/InseeFrLab/formation-python-initiation.git
git clone --depth 1 $REPO_URL $CLONE_DIR

# Install additional packages if a requirements.txt file is present
REQUIREMENTS_FILE=${CLONE_DIR}/requirements.txt
[ -f $REQUIREMENTS_FILE ] && pip install -r $REQUIREMENTS_FILE

# Build notebook from sources
quarto render ${CHAPTER_DIR}/tutorial.qmd --profile ${LANGUAGE} --no-execute --to ipynb --output-dir .

# Fix notebook formatting by removing first empty title
${CLONE_DIR}/utils/fix_ipynb_titles.sh ${CHAPTER_DIR}/tutorial.ipynb

# Put chapter files in the training dir
cp -r ${CHAPTER_DIR}/* ${WORK_DIR}/

# Clean
rm -rf $CLONE_DIR ${WORK_DIR}/tutorial.qmd

# Open the relevant notebook when starting Jupyter Lab
echo "c.LabApp.default_url = '/lab/tree/tutorial.ipynb'" >> /home/onyxia/.jupyter/jupyter_server_config.py
