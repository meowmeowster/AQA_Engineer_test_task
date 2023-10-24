#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import allure
from environment import load_address
from Tests.test_base import BaseTest


@allure.feature('MAIN PAGE')
@allure.severity(allure.severity_level.CRITICAL)
class Tests(BaseTest):

    @pytest.mark.order(3)
    @allure.title("Тестовое задание - проверка UI флоу добавления товара в корзину")
    def test_ui(self):
        self.get_address(load_address())
        assert self.BasePage.is_displayed_element(self, self.MainPage.desktop_logo) is True
        assert self.BasePage.is_displayed_element(self, self.MainPage.hero_shop_mattress) is True
        self.BasePage.check_address(self, load_address())
        self.BasePage.click_on(self, self.MainPage.hero_shop_mattress)
        assert self.BasePage.is_displayed_element(self, self.Mattress.cart_icon) is True
        assert self.BasePage.is_displayed_element(self, self.Mattress.addtocart_btn) is True
        self.BasePage.check_address(self, load_address() + "mattress")
        self.BasePage.click_on(self, self.Mattress.addtocart_btn)
        assert self.BasePage.is_displayed_element(self, self.Cart.summary_title_collapse) is True
        assert self.BasePage.get_element_text(self, self.Cart.summary_title_collapse) == "Order Summary"
        assert self.BasePage.is_displayed_element(self, self.Cart.awara_mattress) is True
        assert self.BasePage.is_displayed_element(self, self.Cart.item_quantity) is True
        assert self.BasePage.get_element_text(self, self.Cart.item_quantity) == "1"
        self.BasePage.check_address(self, load_address() + "checkout/shipping")
        self.BasePage.screenshot(self)

