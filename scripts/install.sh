#!/bin/bash
python -m venv aqa-venv
source aqa-venv/bin/activate
which python
python --version
pwd
ls -la
pip install --upgrade pip
pip install -r ./requirements.txt
docker pull selenoid/chrome:117.0