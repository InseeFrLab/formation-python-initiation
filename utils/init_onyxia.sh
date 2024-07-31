#!/bin/bash

LANGUAGE=$1
SECTION=$2
CHAPTER=$3

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
quarto render $SOURCE_FILE --profile ${LANGUAGE} --no-execute --to ipynb

# Put chapter files in the training dir
if [ "$LANGUAGE" = "fr" ]; then
  DIR_CHAPTER_FILES="${CLONE_DIR}/_site/source/${SECTION}/${CHAPTER}"
elif [ "$LANGUAGE" = "en" ]; then
  DIR_CHAPTER_FILES="${CLONE_DIR}/_site/en/source/${SECTION}/${CHAPTER}"
else
  echo "Unsupported language: $LANGUAGE"
  exit 1
fi
cp -r ${DIR_CHAPTER_FILES}/* ${WORK_DIR}/

# Remove Git repository
rm -r $CLONE_DIR

# Open the relevant notebook when starting Jupyter Lab
echo "c.LabApp.default_url = '/lab/tree/tutorial.ipynb'" >> /home/onyxia/.jupyter/jupyter_server_config.py
