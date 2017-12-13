from d13.main import run, parse, main1, main2

LINES = [
    '0: 3',
    '1: 2',
    '4: 4',
    '6: 4',
]

def test_run():
    instructions = [parse(l) for l in LINES]
    gen = run(instructions, 7)
    assert next(gen) == [3, 2, None, None, 4, None, 4]
    assert next(gen) == [None, None, None, None, None, None, None]
    assert next(gen) == [None, 2, None, None, None, None, None]
    assert next(gen) == [None, None, None, None, None, None, None]
    assert next(gen) == [3, 2, None, None, None, None, None]
    # assert next(gen, 7) == [1, 1, None, None, 1, None, 1]
    # assert next(gen, 7) == [2, 2, None, None, 2, None, 2]
    # assert next(gen, 7) == [3, 1, None, None, 3, None, 3]
    # assert next(gen, 7) == [2, 2, None, None, 4, None, 4]
    # assert next(gen, 7) == [1, 1, None, None, 3, None, 3]

def test_main1():
    assert main1(LINES) == 24

def test_main2():
    assert main2(LINES) == 10
    # assert main2(TEST_INPUT) == 2