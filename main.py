#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options as OptionsChrome


def start_driver(remote):
    options = OptionsChrome()
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--start-maximized")
    options.add_argument("--log-level=3")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument('ignore-certificate-errors')
    if remote:
        driver = webdriver.Remote(
            command_executor="http://172.17.0.4:4444/wd/hub",
            options=options)
    else:
        service = webdriver.ChromeService()
        driver = webdriver.Chrome(service=service, options=options)
    return driver


def stop_driver(driver_instance):
    driver_instance.close()
    driver_instance.quit()


def unix():
    return sys.platform.startswith("linux") or sys.platform.startswith("darwin")


class Steps(unittest.TestCase):
    def get_address(self, driver, address):
        try:
            driver.get(address)
            pass
        except TimeoutException:
            stop_driver(driver)
            self.fail("Exception while trying to connect to " + address)

