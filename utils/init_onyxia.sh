#!/bin/sh

LANGUAGE=$1
SECTION=$2
CHAPTER=$3

WORK_DIR=/home/onyxia/work
CLONE_DIR=${WORK_DIR}/repo-git
COURSE_DIR=${CLONE_DIR}/source/${LANGUAGE}

# Clone course repository
REPO_URL=https://github.com/InseeFrLab/formation-python-initiation.git
git clone --depth 1 $REPO_URL $CLONE_DIR

# Build notebook from sources
SOURCE_FILE=${COURSE_DIR}/${SECTION}/${CHAPTER}/tutorial.qmd
quarto convert $SOURCE_FILE
rm $SOURCE_FILE

# Put chapter files in the training dir
cp -r ${COURSE_DIR}/${SECTION}/${CHAPTER}/* ${WORK_DIR}/

# Install additional packages if needed
REQUIREMENTS_FILE=${CLONE_DIR}/requirements.txt
[ -f $REQUIREMENTS_FILE ] && pip install -r $REQUIREMENTS_FILE && rm $REQUIREMENTS_FILE

# Remove course Git repository
rm -r $CLONE_DIR

# Open the relevant notebook when starting Jupyter Lab
echo "c.LabApp.default_url = '/lab/tree/tutorial.ipynb'" >> /home/onyxia/.jupyter/jupyter_server_config.py
