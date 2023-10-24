#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import sys
from main import start_driver, stop_driver

cicd = sys.platform.startswith("linux") or True


@pytest.fixture()
def setup(request, flag=cicd):
    request.cls.driver = start_driver(flag)
    yield
    if flag:
        request.cls.screenshot(request.cls)
    stop_driver(request.cls.driver)


