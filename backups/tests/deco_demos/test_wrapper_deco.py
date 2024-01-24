import inspect

from revisited.r_decorators.wrapper_deco import WrapperDeco

"""
If you have a function that belongs to a class and you want to pass it as a parameter to another function, you can use the `inspect` module to get the class name of the function at runtime. Here's an example:

```shell
#!/bin/bash

python -c "import inspect

class MyClass:
    def my_function(self):
        pass

def my_other_function(func):
    class_name = inspect.getmembers(func)[0][1].__qualname__.split('.')[-2]
    print(class_name)

my_other_function(MyClass().my_function)"
```

In this example, we define a `MyClass` with a `my_function` method, and a `my_other_function` that takes a function as a parameter. We then call `my_other_function` with an instance of `MyClass` and its `my_function` method as the parameter.

Inside `my_other_function`, we use the `inspect` module to get the fully-qualified name of the passed-in function, and then split the name by the `.` character to get the name of the class that contains the function. Finally, we print the class name.

When you run this script, it will output `MyClass`, which is the name of the class that contains the `my_function` method.
"""


class square_root(WrapperDeco):
    def mutate(self, wrapped, *args, **kwargs):
        members = inspect.getmembers(wrapped)
        sources = inspect.getsource(wrapped)
        call_args = inspect.getcallargs(wrapped, *args, *kwargs)
        # call function which is from a class,
        return wrapped(*args, **kwargs) ** (1 / 2)


class nth_root(WrapperDeco):
    def __init__(self, n=2):
        self.n = n

    def mutate(self, wrapped, *args, **kwargs):
        members = inspect.getmembers(wrapped)
        sources = inspect.getsource(wrapped)
        call_args = inspect.getcallargs(wrapped, *args, *kwargs)
        ## call args: class,
        stack_info = inspect.stack()
        print(members)
        return wrapped(*args, **kwargs) ** (1 / self.n)


@nth_root(n=3)
def get_number(*args, **kwargs):
    return 27


@nth_root
def get_another_number(*args, **kwargs):
    return 16


@square_root
def get_number(*args, **kwargs):
    return 4


class DemoFuncWrapper:

    @nth_root
    def get_another_number(*args, **kwargs):
        return 16


def test_mutate():
    assert get_number(1, 2, 3, 43) == 2.0


def test_mutate_in_class():
    assert DemoFuncWrapper().get_another_number(1, 2, test_arg="test+arg") == 4
