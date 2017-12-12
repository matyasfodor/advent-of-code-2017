STEPS = {
    'nw': (-1, -0.5),
    'n': (-2, 0),
    'ne': (-1, 0.5),
    'sw': (1, -0.5),
    's': (2, 0),
    'se': (1, 0.5),
}

def add_tuple(a, b):
    return tuple(x + y for x, y in zip(a, b))

def distance(pos):
    pos = tuple(abs(c) for c in pos)
    horizontal = pos[1] / 0.5
    vertical = max(pos[0] - horizontal, 0) / 2
    return int(vertical + horizontal)

def main1(steps):
    pos = (0, 0,)
    for s in steps:
        pos = add_tuple(pos, STEPS[s])
    return distance(pos)

def main2(steps):
    pos = (0, 0,)
    max_dist = 0
    for s in steps:
        pos = add_tuple(pos, STEPS[s])
        dist = distance(pos)
        max_dist = dist if dist > max_dist else  max_dist
    return max_dist

if __name__ == '__main__':
    with open('d11/input.txt', 'r') as fp:
        contents = fp.read().split(',')
    print('1: ', main1(contents))
    print('2: ', main2(contents))
