# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
from pyqa_30min.yml_template.yaml_utils import *

#
file_path = "temp.yaml"


def test_load_yaml():
    data = load_yaml(file_path)
    print(data)
#
# def test_load_yaml_structured():
#     data = load_yaml("structured.yaml")
#     print(data)
#
def test_to_yaml_file():
    data = load_yaml("structured.yaml")
    to_yaml_file("test.yaml",data)
