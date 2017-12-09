from d9.main import main1, garbage

def test_main1_1():
    assert main1('{}') == 1

def test_main1_2():
    assert main1('{{{}}}') == 6

def test_main1_3():
    assert main1('{{},{}}') == 5

def test_main1_4():
    assert main1('{{{},{},{{}}}}') == 16

def test_main1_5():
    assert main1('{<a>,<a>,<a>,<a>}') == 1

def test_main1_6():
    assert main1('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9

def test_main1_7():
    assert main1('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 9

def test_main1_8():
    assert main1('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3

def test_garbage_1():
    assert garbage(iter('>')) == 0
    assert garbage(iter('random characters>')) == 17
    assert garbage(iter('<<<>')) == 3
    assert garbage(iter('{!>}>')) == 2
    assert garbage(iter('!!>')) == 0
    assert garbage(iter('!!!>>')) == 0
    assert garbage(iter('{o"i!a,<{i<a>')) == 10
