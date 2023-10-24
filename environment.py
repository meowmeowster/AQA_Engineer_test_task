#!/usr/bin/env python
# -*- coding: utf-8 -*-


def load_address(test_type="UI", log_pass=""):
    if test_type == "API":
        prefix = "https://"
        address = "reqres.in/"
    else:
        prefix = "https://"
        address = "qa.awarasleep.com/"

    return str(prefix + log_pass + address)


