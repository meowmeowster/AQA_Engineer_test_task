source aqa-venv/bin/activate
python -m pytest --no-header -vvv --junitxml results_ui.xml --alluredir=allure-results
exit 0