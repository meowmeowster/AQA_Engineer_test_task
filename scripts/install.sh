#!/bin/bash
python -m venv aqa-venv
. aqa-venv/bin/activate
which python
python --version
cd ..
pwd
pip install --upgrade pip
pip install -r ./requirements.txt