#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import Any

import jinja2
from pydantic.main import BaseModel

tpl_env = jinja2.Environment()


def make_string_template(tpl_str: str) -> jinja2.Template:
    return tpl_env.from_string(tpl_str)


def render_str_template(tpl_str: str, context: Any) -> str:
    tpl = make_string_template(tpl_str)
    return tpl.render(context)


def hello_world():
    return "hello_world"


class StructureClass(BaseModel):
    name: str = "name"
    value: str = "value"


def greeting(name: str):
    return "Hello," + name
def raw_render():
    tpl_str = """
      Hello {{greet(name)}}
      Hello {{ greet(name.upper()) }}
    """
    template = tpl_env.from_string(tpl_str)
    template.globals.update({
        "greet": greeting
    })
    print(template.render(name="test"))


raw_render()


def raw_render_simple():
    tpl_str = """
      "Hello, {{ name.upper() }}!"
      Hello, {{ hello()}}!
      Hello {{greet(name)}}
      Hello {{ greet(name.upper()) }}
      Hello {{clazz.name}}
    """
    template = tpl_env.from_string(tpl_str)
    print(template.render(name="test"))

raw_render_simple()