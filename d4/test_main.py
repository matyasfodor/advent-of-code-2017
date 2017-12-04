from d4.main import valid_line, main1, valid_line2

def test_valid_line():
    assert valid_line('aa bb cc dd ee')
    assert not valid_line('aa bb cc dd aa')
    assert valid_line('aa bb cc dd aaa')

def test_valid_line2():
    assert valid_line2('abcde fghij')
    assert not valid_line2('abcde xyz ecdab')
    assert valid_line2('a ab abc abd abf abj')
    assert valid_line2('iiii oiii ooii oooi oooo')
    assert not valid_line2('oiii ioii iioi iiio')
    