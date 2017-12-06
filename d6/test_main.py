from d6.main import main1, increment

def test_increment():
    assert increment((0, 2, 7, 0,)) == (2, 4, 1, 2,)

def test_main1():
    assert main1((0, 2, 7, 0,)) == 5
