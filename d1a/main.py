# Yields the matching charactersof the input
# circular
from itertools import groupby


def round_iterator(iterator):
    first_element = next(iterator)
    yield first_element
    for i in iterator:
        yield i
    yield first_element

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
