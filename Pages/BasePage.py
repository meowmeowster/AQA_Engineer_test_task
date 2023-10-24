#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import unittest
import pytest
import allure
import traceback
from datetime import datetime
from PIL import Image

lag_multiplier = 1


@pytest.mark.usefixtures("setup")
class BasePage(unittest.TestCase):

    def check_address(self, text):
        with allure.step(f"Пользователь проверяет, что текущий адрес равен \"{text}\""):
            assert self.driver.current_url == text

    def click_on(self, by_locator):
        with allure.step(f"Пользователь кликает на элемент {by_locator}"):
            WebDriverWait(self.driver, 30 * lag_multiplier).until(EC.visibility_of_element_located(by_locator)).click()

    def send_keys_to(self, by_locator, text):
        with allure.step(f"Пользователь вводит текст \"{text}\" в элемент {by_locator}"):
            WebDriverWait(self.driver, 10 * lag_multiplier).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def send_keys_to_array(self, by_locator, text, id):
        with allure.step(f"Пользователь вводит текст \"{text}\" в элемент {by_locator}"):
            WebDriverWait(self.driver, 10 * lag_multiplier).until(EC.presence_of_all_elements_located(by_locator))[id].send_keys(text)

    def send_protected_keys_to(self, by_locator, text):
        with allure.step(f"Пользователь вводит конфиденциальный текст в элемент {by_locator}"):
            WebDriverWait(self.driver, 10 * lag_multiplier).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def clear_field(self, by_locator):
        with allure.step(f"Пользователь очищает поле {by_locator}"):
            WebDriverWait(self.driver, 10 * lag_multiplier).until(EC.visibility_of_element_located(by_locator)).clear()

    def get_element_text(self, by_locator):
        with allure.step(f"Пользователь получает текстовое содержимое элемента {by_locator}"):
            element = WebDriverWait(self.driver, 10 * lag_multiplier).until(EC.visibility_of_element_located(by_locator))
            return element.text

    def is_visible(self, by_locator):
        with allure.step(f"Пользователь проверяет, виден ли элемент {by_locator}"):
            element = WebDriverWait(self.driver, 30 * lag_multiplier).until(EC.visibility_of_element_located(by_locator))
            return bool(element)

    def is_displayed_element(self, by_locator):
        with allure.step(f"Пользователь проверяет, отображается ли элемент {by_locator} на странице"):
            element = WebDriverWait(self.driver, 10 * lag_multiplier).until(EC.visibility_of_element_located(by_locator))
            return element.is_displayed()
        
    def is_not_displayed_element(self, by_locator):
        with allure.step(f"Пользователь проверяет, отображается ли элемент {by_locator} на странице"):
            try:
                WebDriverWait(self.driver, 10 * lag_multiplier).until(EC.presence_of_element_located(by_locator))
            except TimeoutException:
                return True
            return not EC.presence_of_element_located(by_locator)
        
    def is_clickable(self, by_locator):
        with allure.step(f"Пользователь проверяет, кликабелен ли элемент {by_locator} на странице"):
            element = WebDriverWait(self.driver, 10 * lag_multiplier).until(EC.element_to_be_clickable(by_locator))
            return bool(element)

    def is_enabled_element(self, by_locator):
        with allure.step(f"Пользователь проверяет, активен ли элемент {by_locator}"):
            element = WebDriverWait(self.driver, 10 * lag_multiplier).until(EC.visibility_of_element_located(by_locator))
            return element.is_enabled()

    def get_title(self, title):
        with allure.step(f"Пользователь ожидает заголовок {title}"):
            WebDriverWait(self.driver, 10 * lag_multiplier).until(EC.title_is(title))
            return self.driver.title

    def move_to_element(self, by_locator):
        with allure.step(f"Пользователь перемещает страницу к элементу {by_locator}"):
            actions = ActionChains(self.driver)
            actions.move_to_element(
                WebDriverWait(self.driver, 10 * lag_multiplier).until(EC.element_to_be_clickable(by_locator))
            )
            actions.perform()

    def clear(self, by_locator):
        with allure.step(f"Пользователь вручную удаляет текст из поля {by_locator}"):
            WebDriverWait(self.driver, 10 * lag_multiplier).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.CONTROL + "a")
            WebDriverWait(self.driver, 10 * lag_multiplier).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.DELETE)

    def keys_enter(self, by_locator):
        with allure.step(f"Пользователь нажимает Enter, находясь на элементе {by_locator}"):
            WebDriverWait(self.driver, 10 * lag_multiplier).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.ENTER)

    def get_address(self, address):
        with allure.step(f"Пользователь переходит по адресу {address}"):
            self.driver.get(address)
            self.driver.execute_script("window.scrollBy(0,0)", "")
            self.driver.execute_script("scrollBy(0,1);")
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.HOME).perform()

    def screenshot(self, qual=35):
        with allure.step(f"Система делает скриншот страницы и прикладывает его к тестовому отчёту"):
            name = traceback.extract_stack(None, 2)[0][2]
            if name == "setup":
                name = traceback.extract_stack(None, 2)[-1][2]
            else:
                name = name[5:5 + len(name)]
            name_full = name + "_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png"

            self.driver.save_screenshot(name_full)

            picture = Image.open(name_full).convert('RGB')
            name_new = str(qual) + "_" + name + "_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".jpg"
            picture.save(name_new, "JPEG", optimize=True, quality=qual)
            os.remove(name_full)

            allure.attach(open(name_new, 'rb').read(), attachment_type=allure.attachment_type.JPG)

