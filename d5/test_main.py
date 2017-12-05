from d5.main import main1, main2

def test_main1():
    assert main1([0, 3, 0, 1, -3]) == 5

def test_main2():
    assert main2([0, 3, 0, 1, -3]) == 10
