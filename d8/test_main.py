from d8.main import main1, main2

LINES = [
    'b inc 5 if a > 1',
    'a inc 1 if b < 5',
    'c dec -10 if a >= 1',
    'c inc -20 if c == 10',
]

def test_main1():
    assert main1(LINES) == 1

def test_main2():
    assert main2(LINES) == 10
