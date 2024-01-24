#!/usr/bin/env python
# -*- coding:utf-8 -*-
import rich
import revisited.r_jsons as json_all


def test_decode_json():
    rich.print(json_all.decode_json())


def test_encode_json():
    rich.print_json(json_all.encode_json())
