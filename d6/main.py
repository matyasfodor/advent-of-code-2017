from itertools import count
import functools

def with_index(func, array, **kwargs):
    key_func = kwargs.get('key', lambda x: x)
    return func(enumerate(array), key=lambda v: key_func(v[1]))


min_with_index = functools.partial(with_index, min)

max_with_index = functools.partial(with_index, max)


def increment(state):
    state = list(state)
    max_index, max_value = max_with_index(state)
    state[max_index] = 0
    # not the smartest solution, but it'll do it for now
    for i in range(max_index, max_index + max_value):
        state[(i + 1) % len(state)] += 1
    return tuple(state)


def main1(state):
    cache = set()
    for i in count():
        state = increment(state)
        if state in cache:
            return i + 1, state
        cache.add(state)

def main2(contents):
    _, stop_point = main1(contents)
    state = stop_point
    for i in count():
        state = increment(state)
        if state == stop_point:
            return i + 1

if __name__ == '__main__':
    with open('d6/input.txt') as fp:
        contents = tuple([int(w) for w in fp.readline().split()])
    print('1: ', main1(contents)[0])
    print('2: ', main2(contents))
