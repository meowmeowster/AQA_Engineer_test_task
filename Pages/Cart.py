#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
import pytest


@pytest.mark.usefixtures("setup")
class Cart(BasePage):

    summary_title_collapse = (By.CSS_SELECTOR, '[data-testid="summary_title_collapse"]')
    awara_mattress = (By.CSS_SELECTOR, '[data-testid="awara-latex-hybrid-mattress"]')
    item_quantity = (By.CSS_SELECTOR, '[data-testid="item-quantity"]')