from collections import Counter

def valid_line(line):
    counter = Counter(line.split(' '))
    most_common, = counter.most_common(1)
    _, freq = most_common
    return freq == 1

def main1(lines):
    counter = 0
    for line in lines:
        if valid_line(line):
            counter += 1
    return counter

def valid_line2(line):
    counter = Counter([''.join(sorted(w)) for w in line.split(' ')])
    most_common, = counter.most_common(1)
    _, freq = most_common
    return freq == 1

def main2(lines):
    counter = 0
    for line in lines:
        if valid_line2(line):
            counter += 1
    return counter

if __name__ == '__main__':
    with open('d4/input.txt', 'r') as fp:
        contents = [l.strip() for l in fp.readlines()]
    print('1: ', main1(contents))
    print('2: ', main2(contents))
    