#!/bin/bash
python -m venv aqa-venv
. aqa-venv/bin/activate
which python
python --version
pwd
ls -la
pip install --upgrade pip
pip install -r ./requirements.txt