# Yields the matching charactersof the input
# circular
import collections
from itertools import takewhile, islice, tee, groupby


# Source https://docs.python.org/3/library/itertools.html#itertools-recipes
def consume(iterator, n):
    "Advance the iterator n-steps ahead. If n is none, consume entirely."
    return islice(iterator, n, None)


def equals(a):
    def inner(b):
        return a == b
    return inner


def round_iterator(iterator):
    first_element = next(iterator)
    yield first_element
    for i in iterator:
        yield i
    yield first_element

def take_equals():
    value = None
    def inner(new_value):
        nonlocal value
        if value is None:
            value = new_value
        # print('##: ', value, new_value)
        return value == new_value
    return inner

def yield_matching_copyfree(string):
    index = 0
    while index < len(string):
        # ret = ''.join(takewhile(take_equals(), iter))
        ret = ''.join(takewhile(take_equals(), consume(string, index)))
        index += len(ret)
        yield ret


def yield_matching_iter2(it):
    value = next(it)
    while True:
        counter = 1
        while True:
            new_value = next(it)
            if new_value == value:
                counter +=1
            else:
                # backward compatibility
                yield [value for _ in range(counter)]
                value = new_value
                continue
    yield [4]


def yield_matching_iter(it):
    while True:
        it, copy = tee(it)
        value = list(takewhile(take_equals(), it))
        consume(it, len(value))
        if len(value) > 0:
            yield value
        else:
            break


def yield_matching(string):
    return yield_matching_copyfree(string)
    # while len(string):
    #     ret = ''.join(takewhile(lambda c: c == string[0], string))
    #     string = string[len(ret):]
    #     yield ret

def aggregate(k, g):
    g = list(g)
    return k * (len(g) -1)

def main(content):
    content = [int(c) for c in content]
    return sum([aggregate(k, g) for k, g in groupby(round_iterator(iter(content)))])

if __name__ == '__main__':
    with open('input.txt') as fp:
        content = fp.read().strip()
    main(content)
