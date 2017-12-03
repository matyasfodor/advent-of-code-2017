# Yields the matching charactersof the input
# circular
import collections
from itertools import takewhile, islice


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
        print('##: ', value, new_value)
        return value == new_value
    return inner

def yield_matching_copyfree(string):
    index = 0
    while index < len(string):
        # ret = ''.join(takewhile(take_equals(), iter))
        ret = ''.join(takewhile(take_equals(), consume(string, index)))
        index += len(ret)
        yield ret


def yield_matching(string):
    return yield_matching_copyfree(string)
    # while len(string):
    #     ret = ''.join(takewhile(lambda c: c == string[0], string))
    #     string = string[len(ret):]
    #     yield ret

def aggregate(seq):
    return seq[0] * (len(seq) - 1)

def main(content):
    content = [int(c) for c in content]
    return sum([aggregate(seq) for seq in yield_matching_copyfree(iter(content))])

if __name__ == '__main__':
    with open('input.txt') as fp:
        content = fp.read().strip()
    main(content)
