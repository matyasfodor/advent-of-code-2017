from d15.main import main1, main2, parse_input, next_val_gen

LINES = [
    'Generator A starts with 783',
    'Generator B starts with 325',
]

def test_parse_input():
    val = parse_input(LINES)
    assert {'A': 783, 'B': 325} == val

def test_main1():
    assert main1({'A': 65, 'B': 8921}) == 588

def test_next_val_gen_4():
    gen = next_val_gen(65, 16807, 2147483647, 4)
    assert next(gen) == 1352636452
    assert next(gen) == 1992081072
    assert next(gen) == 530830436
    assert next(gen) == 1980017072
    assert next(gen) == 740335192

def test_next_val_gen_8():
    gen = next_val_gen(8921, 48271, 2147483647, 8)
    assert next(gen) == 1233683848
    assert next(gen) == 862516352
    assert next(gen) == 1159784568
    assert next(gen) == 1616057672
    assert next(gen) == 412269392

def test_main2():
    assert main2({'A': 65, 'B': 8921}) == 309
