from main import yield_matching, round_iterator, main


def test_yield_matching_different_chars():
    assert list(yield_matching('abcdef')) == list('abcdef')

def test_yeild_duplicates():
    assert list(yield_matching('aabcde')) == ['aa', 'b', 'c', 'd', 'e'
]

def test_round_iterator():
    assert list(round_iterator([1, 2, 3, 4].__iter__())) == [1, 2, 3, 4, 1]


def test_main():
    assert main('1122') == 3
    assert main('1111') == 4
    assert main('1234') == 0
    assert main('91212129') == 9
