#!/bin/bash
source aqa-venv/bin/activate
allure generate --report-dir allure-report allure-results
ls -la