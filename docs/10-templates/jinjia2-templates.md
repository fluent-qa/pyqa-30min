# Jinja2 Templates

模版引擎:
> A template engine or template processor is a library designed
> to combine templates with a data model to produce documents.

## 1. 实例化

```python
def what_is_template():
    name = input("Enter your name: ")
    tm = Template("Hello {{ name }}")
    msg = tm.render(name=name)
    print(msg)
```

1. 模板：

```python
"Hello {{ name }}"
```

2. 数据: name, 输入之后返回为:

```shell
Enter your name: Revisited-QA
Hello Revisited-QA
```

3. 模版说明

```shell
{% %} - statements
{{ }} - expressions to print to the template output
{# #} - comments which are not included in the template output
# ## - line statements
```

## 模版和更多的数据

```python
def template_with_more_data(**kwargs):
    tm = Template("My name is {{ name }} and I am {{ age }}")
    msg = tm.render(**kwargs)
    print(msg)
```

一下函数的打印结果是什么？

```python
template_with_more_data(name="John", age=27)
```

结果：

```shell
My name is John and I am 27
```

## 模板和结构化数据: 类/字典

```shell
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getAge(self):
        return self.age
    def getName(self):
        return self.name

def template_with_class():
    person = Person('Peter', 34)
    tm = Template("My name is {{ per.getName() }} and I am {{ per.getAge() }}")
    msg = tm.render(per=person)
    print(msg)
def template_with_dict():
    person = {"name": "Alice", "age": 12}
    tm = Template("My name is {{ per.name }} and I am {{ per.age }}")
    
    msg = tm.render(per=person)
    print(msg)
```

