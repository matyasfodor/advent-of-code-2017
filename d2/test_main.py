from d2.main import main1, evenly_divisible, main2

def test_main1():
    assert main1([
        '5 1 9 5',
        '7 5 3',
        '2 4 6 8',
    ]) == 18

def test_evenly_divisible():
    assert evenly_divisible([5, 9, 2, 8]) == 4
    assert evenly_divisible([9, 4, 7, 3]) == 3
    assert evenly_divisible([3, 8, 6, 5]) == 2

def test_main2():
    assert main2([
        '5 9 2 8',
        '9 4 7 3',
        '3 8 6 5',
    ]) == 9
