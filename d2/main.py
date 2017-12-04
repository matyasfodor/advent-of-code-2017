def evenly_divisible(values):
    values.sort(reverse=True)
    for index, divident in enumerate(values):
        for divisor in values[index+1:]:
            if divident % divisor == 0:
                return int(divident / divisor)


def main1(contents):
    agg = 0
    for row in contents:
        line = [int(c) for c in row.strip().split()]
        agg += max(line) - min(line)
    return agg

def main2(contents):
    agg = 0
    for row in contents:
        line = [int(c) for c in row.strip().split()]
        agg += evenly_divisible(line)
    return agg

if __name__ == '__main__':
    with open('d2/input.txt') as fp:
        contents = fp.readlines()
    print('1: ', main1(contents))
    print('2: ', main2(contents))
