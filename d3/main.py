def frame_sizes():
    agg = 0
    yield 1
    while True:
        agg += 8
        yield agg

def nth_frame(n):
    if n > 0:
        return 8 * (n - 1)
    else:
        return 1

def frame_number(value):
    agg = 0
    for index, frame in enumerate(frame_sizes()):
        if value <= agg:
            return index, agg
        agg += frame

def main1(value):
    number, full_frame_number = frame_number(value)
    frame_size = nth_frame(number)
    side_length = frame_size / 4
    frames_sofar = full_frame_number - frame_size
    offset = abs((value - frames_sofar) % side_length - (side_length / 2))
    return int(offset + (number - 1))


def add_tuples(a, b):
    return tuple([sum(pair) for pair in zip(a, b)])

def turn_left(prev):
    new = tuple(reversed(prev))
    if new[0] != 0:
        new = tuple([-1 * x for x in new])
    return new

def nex_pos():
    position = (0, 0,)
    direction = (1, 0,)
    side_length = 1
    while True:
        for _ in range(2):
            for _ in range(side_length):
                yield position
                position = add_tuples(position, direction)
            direction = turn_left(direction)
        side_length += 1

def neighbours(pos):
    for i in range(-1, 2):
        for j in range(-1, 2):
            yield add_tuples(pos, (i, j,))

def main2(value):
    gen = nex_pos()
    first_pos = next(gen)
    lookup = {
        first_pos: 1
    }
    while True:
        new_pos = next(gen)
        new_value = sum([lookup.get(neighbor, 0) for neighbor in neighbours(new_pos)])
        if new_value > value:
            return new_value
        lookup[new_pos] = new_value


if __name__ == '__main__':
    value = 289326
    print('1: ', main1(value))
    print('2: ', main2(value))
