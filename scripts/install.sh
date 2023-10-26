#!/bin/bash
python -m venv aqa-venv
source aqa-venv/bin/activate
which python
python --version
pwd
ls -la
pip install --upgrade pip
pip install -r ./requirements.txt
sudo apt update
sudo apt install openjdk-8-jdk
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
echo $JAVA_HOME