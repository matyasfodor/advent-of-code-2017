def garbage(contents):
    ignore = False
    collected = 0
    for c in contents:
        if ignore:
            ignore = False
            continue
        elif c == '>':
            return collected
        elif c == '!':
            ignore = True
            continue
        collected += 1
    return collected

def inner(contents, base_score):
    sum_score = 0
    score = base_score + 1
    ignore = False
    for c in contents:
        if ignore:
            ignore = False
            continue
        elif c == '{':
            sum_score += inner(contents, score)
        elif c == '!':
            ignore = True
        elif c == '<':
            garbage(contents)
        elif c == '}':
            return score + sum_score
    return score + sum_score

def main1(contents):
    return inner(iter(contents), -1)

def main2(contents):
    sum_garbage = 0
    contents = iter(contents)
    ignore = False
    for c in contents:
        if ignore:
            ignore = False
            continue
        elif c == '!':
            ignore = True
            continue
        elif c == '<':
            sum_garbage += garbage(contents)
    return sum_garbage

if __name__ == '__main__':
    with open('d9/input.txt', 'r') as fp:
        contents = fp.read().strip()
    print('1: ', main1(contents))
    print('2: ', main2(contents))
