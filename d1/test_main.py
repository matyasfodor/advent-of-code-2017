from d1a.main import round_iterator, main1, main2


def test_round_iterator():
    assert list(round_iterator([1, 2, 3, 4].__iter__())) == [1, 2, 3, 4, 1]


def test_main1():
    assert main1('1122') == 3
    assert main1('1111') == 4
    assert main1('1234') == 0
    assert main1('91212129') == 9


def test_main2():
    assert main2('1212') == 6
    assert main2('1221') == 0
    assert main2('123425') == 4
    assert main2('123123') == 12
    assert main2('12131415') == 4
    