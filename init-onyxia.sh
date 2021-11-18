#!/bin/sh

# Clone course repository
REPO_URL=https://github.com/InseeFrLab/formation-python-initiation.git
WORK_DIR=/home/jovyan/work
CLONE_DIR=${WORK_DIR}/repo-git
git clone --recurse-submodules --depth 1 $REPO_URL $CLONE_DIR

# Put relevant notebook in the working dir
# The `CHAPTER` and `NOTEBOOK` variables are passed from a Vault secret specified in the launch URL
COURSE_DIR=${WORK_DIR}/repo-git/course
FORMATION_DIR=${WORK_DIR}/formation-python
mkdir $FORMATION_DIR
cp ${COURSE_DIR}/${CHAPTER}/${IPYNB_NAME}.ipynb ${FORMATION_DIR}/
# Put solutions file in work
cp ${COURSE_DIR}/${CHAPTER}/solutions/${IPYNB_NAME}.py ${WORK_DIR}/solutions.py
# Give appropriate permissions to allow editing notebook
chown -R jovyan:users $FORMATION_DIR

# Install additional packages if needed
REQUIREMENTS_FILE=${COURSE_DIR}/${CHAPTER}/requirements/${IPYNB_NAME}.txt
[ -f $REQUIREMENTS_FILE ] && pip install -r $REQUIREMENTS_FILE

# Remove clone repository
rm -r $CLONE_DIR

# Open the relevant notebook when starting Jupyter Lab
echo "c.LabApp.default_url = '/lab/tree/formation-python/${IPYNB_NAME}.ipynb'" >> /home/jovyan/.jupyter/jupyter_server_config.py
