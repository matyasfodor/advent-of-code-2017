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

def main1(content):
    content = [int(c) for c in content]
    return sum([aggregate(k, g) for k, g in groupby(round_iterator(iter(content)))])


def main2(content):
    content = [int(c) for c in content]
    halway = int(len(content) / 2)
    return sum([f + r for f, r in zip(content[:halway], content[halway:]) if f == r])

if __name__ == '__main__':
    with open('d1a/input.txt') as fp:
        content = fp.read().strip()
    print('1: ', main1(content))
    print('2: ', main2(content))
