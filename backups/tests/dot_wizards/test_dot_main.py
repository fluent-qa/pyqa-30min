from revisited.r_data.dot_wizards.dot_main import make_dot_wiz, DotAccessor


def test_make_dot_wiz():
    result = make_dot_wiz([('k1', 11), ('k2', [{'a': 'b'}]), ('k3', 'v3')], y=True)
    print(result)
    print(result.to_dict())
    print(result.k1)
    dd = make_dot_wiz([(1, 'test'), ('two', [{'hello': 'world'}])],
                      a=1, b='two', c={'d': [123]})

    assert repr(dd) == "*(a=1, b='two', c=*(d=[123]), 1='test', two=[*(hello='world')])"
    assert dd.a == 1
    assert dd.b == 'two'
    assert dd[1] == 'test'
    assert dd.two == [DotAccessor(hello='world')]
    assert dd.c.d[0] == 123

    dd.b = [1, 2, 3]
    assert dd.b == [1, 2, 3]