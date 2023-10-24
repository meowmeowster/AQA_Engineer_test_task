#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import allure
import requests


class API(unittest.TestCase):
    def execute_request(self, url, method, payload=None):
        with allure.step(f"Пользователь исполняет запрос \"{method}\" по адресу \"{url}\""):
            if method == "GET":
                self.response = requests.get(url)
            elif method == "POST":
                self.response = requests.post(url, payload)
            elif method == "PATCH":
                self.response = requests.patch(url, payload)
            elif method == "PUT":
                self.response = requests.put(url, payload)
            elif method == "DELETE":
                self.response = requests.delete(url)
            else:
                self.response = requests.get(url)
            return self.response
