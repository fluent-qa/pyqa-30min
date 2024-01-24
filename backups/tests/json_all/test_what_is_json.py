#!/usr/bin/env python
# -*- coding:utf-8 -*-
import rich

from pyqa_30min.json_all import what_is_json
from pyqa_30min.json_all.what_is_json import json_to_dict


def test_json_to_dict():
    result = json_to_dict()
    print(type(result))
    print(result['population'])

def test_read_json_file():
    result = what_is_json.read_json_file()
    rich.print(type(result))
    rich.print(result['population'])