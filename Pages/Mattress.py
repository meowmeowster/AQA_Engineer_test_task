#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
import pytest


@pytest.mark.usefixtures("setup")
class Mattress(BasePage):

    addtocart_btn = (By.CSS_SELECTOR, '[data-testid="addtocart_btn"]')
    cart_icon = (By.CSS_SELECTOR, '[data-testid="cart-icon"]')
