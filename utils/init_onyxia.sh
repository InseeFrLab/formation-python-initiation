#!/bin/bash

SECTION=$1
CHAPTER=$2
LANGUAGE=$3

WORK_DIR=/home/onyxia/work
CLONE_DIR=${WORK_DIR}/repo-git

# Clone course repository
REPO_URL=https://github.com/InseeFrLab/formation-python-initiation.git
git clone --depth 1 $REPO_URL $CLONE_DIR

# Install additional packages if a requirements.txt file is present
REQUIREMENTS_FILE=${CLONE_DIR}/requirements.txt
[ -f $REQUIREMENTS_FILE ] && pip install -r $REQUIREMENTS_FILE

# Build notebook from sources
SOURCE_FILE=${CLONE_DIR}/source/${SECTION}/${CHAPTER}/tutorial.qmd
quarto render $SOURCE_FILE --profile ${LANGUAGE:-fr} --no-execute --to ipynb

# Put chapter files in the training dir
cp -r ${CLONE_DIR}/_site/${LANGUAGE}/source/${SECTION}/${CHAPTER}/* ${WORK_DIR}/

# Remove Git repository
rm -r $CLONE_DIR

# Open the relevant notebook when starting Jupyter Lab
echo "c.LabApp.default_url = '/lab/tree/tutorial.ipynb'" >> /home/onyxia/.jupyter/jupyter_server_config.py
