#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import pytest
import allure

from environment import load_address
from Tests.test_base import API, BaseTestAPI


@allure.feature('API')
@allure.severity(allure.severity_level.CRITICAL)
class Tests(BaseTestAPI):

    @pytest.mark.order(4)
    @allure.title("Тестовое задание - создание пользователя методом POST")
    def test_post_create_user(self):
        result = API.execute_request(self, load_address("API") + "api/users", "POST",
                                          '{"name": "morpheus", "job": "test0"}')
        assert result.status_code == 201
        response = json.loads(result.text)
        for i in ['id', 'createdAt']:
            assert i in list(response)

    @pytest.mark.order(5)
    @allure.title("Тестовое задание - получение данных пользователя 12 методом GET")
    def test_get_single_user(self):
        result = API.execute_request(self, load_address("API") + "api/users/12", "GET")
        assert result.status_code == 200
        response = json.loads(result.text)
        for i in ['data', 'support']:
            assert i in list(response)

    @pytest.mark.order(6)
    @allure.title("Тестовое задание - изменение данных пользователя 12 методом PATCH")
    def test_patch_single_user(self):
        result = API.execute_request(self, load_address("API") + "api/users/12", "PATCH",
                                          '{"name": "morpheus", "job": "test1"}')
        assert result.status_code == 200
        response = json.loads(result.text)
        for i in ['updatedAt']:
            assert i in list(response)

    @pytest.mark.order(7)
    @allure.title("Тестовое задание - изменение данных пользователя 12 методом PUT")
    def test_put_single_user(self):
        result = API.execute_request(self, load_address("API") + "api/users/12", "PUT",
                                          '{"name": "morpheus", "job": "test2"}')
        assert result.status_code == 200
        response = json.loads(result.text)
        for i in ['updatedAt']:
            assert i in list(response)

    @pytest.mark.order(8)
    @allure.title("Тестовое задание - удаление данных пользователя 12 методом DELETE")
    def test_delete_single_user(self):
        result = API.execute_request(self, load_address("API") + "api/users/12", "DELETE")
        assert result.status_code == 204
        assert result.text == ''
