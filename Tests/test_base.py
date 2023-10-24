#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Pages.BasePage import BasePage
from Pages.API import API


class BaseTestUI(BasePage):
    from Pages.BasePage import BasePage
    from Pages.MainPage import MainPage
    from Pages.Mattress import Mattress
    from Pages.Cart import Cart

    pass


class BaseTestAPI(API):
    from Pages.API import API

    pass
