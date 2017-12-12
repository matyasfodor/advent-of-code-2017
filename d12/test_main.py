from d12.main import parse_line, main1, main2

def test_parse_line():
    assert parse_line('0 <-> 2') == ('0', ['2'])
    assert parse_line('2 <-> 0, 3, 4') == ('2', ['0', '3', '4'])

TEST_INPUT = [
    '0 <-> 2',
    '1 <-> 1',
    '2 <-> 0, 3, 4',
    '3 <-> 2, 4',
    '4 <-> 2, 3, 6',
    '5 <-> 6',
    '6 <-> 4, 5',
]

def test_main1():
    assert main1(TEST_INPUT) == 6

def test_main2():
    assert main2(TEST_INPUT) == 2