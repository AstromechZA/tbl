from builtins import bytes

from tbl.table import tablify


def test_tablify_none():
    assert tablify(None) == [['None']]


def test_tablify_row():
    assert tablify([1, 2]) == [['1'], ['2']]


def test_tablify_str():
    assert tablify('something') == [['something']]


def test_stablify_bytes():
    assert tablify(bytes(b'blah')) == [["b'blah'"]]
