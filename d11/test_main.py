from d11.main import add_tuple, main1

def test_add_tuple():
    assert add_tuple((4, 5), (7, 9)) == (11, 14,)

def test_main1():
    assert main1(['ne', 'ne', 'ne']) == 3
    assert main1(['ne', 'ne', 'sw', 'sw']) == 0
    assert main1(['ne', 'ne', 's', 's']) == 2
    assert main1(['se', 'sw', 'se', 'sw', 'sw']) == 3
