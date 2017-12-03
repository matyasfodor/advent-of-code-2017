from d1a.main import round_iterator, main


def test_round_iterator():
    assert list(round_iterator([1, 2, 3, 4].__iter__())) == [1, 2, 3, 4, 1]


def test_main():
    assert main('1122') == 3
    assert main('1111') == 4
    assert main('1234') == 0
    assert main('91212129') == 9
