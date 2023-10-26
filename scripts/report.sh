#!/bin/bash
source aqa-venv/bin/activate
allure generate --report-dir allure-report
cd allure-report
ls -la