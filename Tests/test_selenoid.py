#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import allure
from environment import load_address
from Tests.test_base import BaseTest


@allure.feature('SERVICE SMOKE')
@allure.severity(allure.severity_level.BLOCKER)
class Tests(BaseTest):

    @pytest.mark.order(1)
    @allure.title("Проверка, что контейнер с браузером успешно запускается")
    @pytest.mark.dependency(name="selenoid_running")
    def test_selenoid(self):
        ...

    @pytest.mark.order(2)
    @allure.title("Проверка, что сервер проекта работоспособен и адрес указан верно")
    @pytest.mark.dependency(depends=['selenoid_running'])
    def test_site_opening(self):
        self.get_address(load_address())
        assert self.BasePage.is_displayed_element(self, self.MainPage.desktop_logo) is True
        self.BasePage.screenshot(self)
