from revisited.r_di.injectable import Injectable
from revisited.r_di.utils import describe, get_dependency_name


def test_describe():
    print(describe("test"))

def test_get_dependency_name():
    result = get_dependency_name("test")
    print(result)
    result = get_dependency_name(ProcessLookupError)
    print(result)