#!/usr/bin/env python
# -*- coding:utf-8 -*-

import rich

from pyqa_30min import json_all


def test_json_to_class():
    rich.print(json_all.json_to_class())


def test_dict_to_class():
    rich.print(json_all.dict_to_class())


def test_class_to_dict():
    rich.print(json_all.class_to_dict())


def test_class_to_json():
    rich.print(json_all.class_to_json())
