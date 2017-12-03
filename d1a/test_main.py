from d1a.main import yield_matching, round_iterator, main, take_equals, yield_matching_iter2


def test_yield_matching_different_chars():
    assert list(yield_matching('abcdef')) == list('abcdef')

def test_yeild_duplicates():
    assert list(yield_matching('aabcde')) == ['aa', 'b', 'c', 'd', 'e']

def test_round_iterator():
    assert list(round_iterator([1, 2, 3, 4].__iter__())) == [1, 2, 3, 4, 1]

# def test_yield_matching_iter():
#     print('%#%#%#%', list(yield_matching_iter2(iter([1, 1,2,2]))))
#     assert list(yield_matching_iter2(iter([1, 2, 3, 4]))) == [[1],[2],[3],[4]]
#     assert list(yield_matching_iter2(iter([1, 1,2,2]))) == [[1,1], [2,2]]


def test_take_equals():
    func = take_equals()
    func(5)
    assert func(5)
    assert not func(6)
    other_func = take_equals()
    other_func(11)
    assert other_func(11)
    assert func(5)
    assert not other_func(5)


def test_main():
    assert main('1122') == 3
    assert main('1111') == 4
    assert main('1234') == 0
    assert main('91212129') == 9
