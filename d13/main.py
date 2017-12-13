from collections import deque
from itertools import islice, count

def run(instructions, length):
    vector = [None] * length
    gradient = [None] * length
    state = [None] * length
    for (place, size) in instructions:
        vector[place] = size
        gradient[place] = 1
        state[place] = 1
    
    while True:
        yield [vector[i] if state[i] == 1 else None for i in range(length)]
        for i in range(length):
            if state[i] is None:
                continue
            state[i] += gradient[i]
            if state[i] in (1, vector[i]):
                gradient[i] *= -1

def parse(line):
    return [int(c) for c in line.split(': ')]

def main1(rules):
    instructions = [parse(l) for l in rules]
    length = max([i[0] for i in instructions]) + 1
    position = 0
    suffer_score = 0
    for i, state in zip(range(length), run(instructions, length)):
        if state[i] is not None:
            suffer_score += i * state[i]
    return suffer_score

def yield_paths(instructions, length):
    gen = run(instructions, length)
    dq = deque(iterable=islice(gen, length), maxlen=length)
    while True:
        path = [dq[i][i] for i in range(length)]
        yield path
        dq.append(next(gen))

def main2(rules):
    instructions = [parse(l) for l in rules]
    length = max([i[0] for i in instructions]) + 1
    for i, path in zip(count(), yield_paths(instructions, length)):
        # print('####: ', path)
        # import time; time.sleep(1)
        if all([s is None for s in path]):
            return i


if __name__ == '__main__':
    with open('d13/input.txt', 'r') as fp:
        contents = [l.strip() for l in fp.readlines()]
    print('1: ', main1(contents))
    print('2: ', main2(contents))
