#!/bin/bash
source aqa-venv/bin/activate
cd allure-results
allure generate --report-dir allure-report
ls -la