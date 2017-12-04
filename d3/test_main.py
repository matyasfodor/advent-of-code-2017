from  d3.main import (frame_sizes, frame_number, nth_frame, main1,
                      add_tuples, turn_left, nex_pos, neighbours)

def test_frame_sizes():
    gen = frame_sizes()
    assert next(gen) == 1
    assert next(gen) == 8
    assert next(gen) == 16


def test_nth_frame():
    assert nth_frame(1) == 0
    assert nth_frame(2) == 8
    assert nth_frame(3) == 16


def test_frame_number():
    assert frame_number(1) == (1, 1)
    assert frame_number(2) == (2, 9)
    assert frame_number(9) == (2, 9)
    assert frame_number(10) == (3, 25)
    assert frame_number(25) == (3, 25)

def test_main1():
    assert main1(12) == 3
    assert main1(23) == 2
    assert main1(1024) == 31

def test_add_tuples():
    assert add_tuples((0, 3), (9, 0)) == (9, 3,)

def test_turn_left():
    assert turn_left((1, 0,)) == (0, 1,)
    assert turn_left((0, 1,)) == (-1, 0,)
    assert turn_left((-1, 0,)) == (0, -1,)
    assert turn_left((0, -1,)) == (1, 0,)

def test_nex_pos():
    gen = nex_pos()
    positions = [next(gen) for _ in range(25)]
    assert positions[0] == (0, 0)
    assert positions[1] == (1, 0)
    assert positions[2] == (1, 1)
    assert positions[3] == (0, 1)
    assert positions[9] == (2, -1)
    assert positions[12] == (2, 2)
    assert positions[16] == (-2, 2)
    assert positions[20] == (-2, -2)
    assert positions[24] == (2, -2)

def test_neighbours():
    positions = {e for e in neighbours((0,0))}
    assert positions == {(-1, -1,), (-1, 0,), (-1, 1,),
                         (0, -1,), (0, 0,), (0, 1,),
                         (1, -1,), (1, 0,), (1, 1,),}
