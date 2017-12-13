from d10.main import round, twist, hexa_convert, main2

def test_twist():
    assert twist([0, 1, 2, 3, 4], 0, 3) == [2, 1, 0, 3, 4]
    assert twist([2, 1, 0, 3, 4], 3, 4) == [4, 3, 0, 1, 2]
    assert twist([4, 3, 0, 1, 2], 1, 1) == [4, 3, 0, 1, 2]
    assert twist([4, 3, 0, 1, 2], 1, 5) == [3, 4, 2, 1, 0]

def test_round():
    assert round([3, 4, 1, 5], list(range(5))) == ([3, 4, 2, 1, 0], 4, 4)

def test_hexa_convert():
    assert hexa_convert([64, 7, 255]) == '4007ff'

def test_main2_1():
    # assert main2('') == 'a2582a3a0e66e6e86e3812dcb672a272'
    assert main2('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
