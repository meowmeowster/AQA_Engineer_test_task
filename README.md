# AQA_Engineer_test_task


Флоу запуска тестов локально с исполнением на удалённой машине: 


pip install --upgrade pip

pip install -r ./requirements.txt

python -m pytest


Для запуска на своём докер-контейнере необходимо сменить IP на 127.0.0.1 в main.py: 

command_executor="http://127.0.0.1:4444/wd/hub"
