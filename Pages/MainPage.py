#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
import pytest


@pytest.mark.usefixtures("setup")
class MainPage(BasePage):

    desktop_logo = (By.CSS_SELECTOR, '[data-testid="desktop_logo"]')
    hero_shop_mattress = (By.CSS_SELECTOR, '[data-testid="hero_shop_mattress"]')

