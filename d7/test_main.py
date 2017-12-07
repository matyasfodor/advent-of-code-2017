from d7.main import main1, parse, outlier, main2

def test_parse():
    assert ('pbga', 66, [],) == parse('pbga (66)')
    assert ('fwft', 72, ['ktlj', 'cntj', 'xhth']) == parse('fwft (72) -> ktlj, cntj, xhth')

LINES = ['pbga (66)',
    'xhth (57)',
    'ebii (61)',
    'havc (66)',
    'ktlj (57)',
    'fwft (72) -> ktlj, cntj, xhth',
    'qoyq (66)',
    'padx (45) -> pbga, havc, qoyq',
    'tknk (41) -> ugml, padx, fwft',
    'jptl (61)',
    'ugml (68) -> gyxo, ebii, jptl',
    'gyxo (61)',
    'cntj (57)',]

def test_main1():
    assert main1(LINES) == 'tknk'

def test_main2():
    assert main2(LINES) == 60

def test_outlier():
    assert outlier([1, 2, 2]) == 1
    assert outlier([2, 3, 2]) == 3
    assert outlier([3, 3, 1]) == 1
    assert outlier([3, 3, 3]) == None
    assert outlier([3, 3, 1, 3, 3]) == 1
    assert outlier([3, 3, 9, 3, 3]) == 9
    assert outlier([3, 3, 14, 3]) == 14
