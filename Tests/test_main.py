#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import allure
from environment import load_address
from Tests.test_base import *


@allure.feature('MAIN PAGE')
@allure.severity(allure.severity_level.CRITICAL)
class Tests(BaseTestUI):

    @pytest.mark.order(3)
    @allure.title("Тестовое задание - проверка UI флоу добавления товара в корзину")
    def test_ui(self):
        self.get_address(load_address())
        assert BasePage.is_displayed_element(self, MainPage.desktop_logo) is True
        assert BasePage.is_displayed_element(self, MainPage.hero_shop_mattress) is True
        BasePage.check_address(self, load_address())
        BasePage.click_on(self, MainPage.hero_shop_mattress)
        assert BasePage.is_displayed_element(self, Mattress.cart_icon) is True
        assert BasePage.is_displayed_element(self, Mattress.addtocart_btn) is True
        BasePage.check_address(self, load_address() + "mattress")
        BasePage.click_on(self, Mattress.addtocart_btn)
        assert BasePage.is_displayed_element(self, Cart.summary_title_collapse) is True
        assert BasePage.get_element_text(self, Cart.summary_title_collapse) == "Order Summary"
        assert BasePage.is_displayed_element(self, Cart.awara_mattress) is True
        assert BasePage.is_displayed_element(self, Cart.item_quantity) is True
        assert BasePage.get_element_text(self, Cart.item_quantity) == "1"
        BasePage.check_address(self, load_address() + "checkout/shipping")
        BasePage.screenshot(self)

