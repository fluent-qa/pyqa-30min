#!/usr/bin/env python
# -*- coding:utf-8 -*-
import rich

from pyqa_30min import json_all


def test_dict_to_json():
    rich.print_json(json_all.dict_to_json())
