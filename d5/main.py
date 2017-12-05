def main1(numbers):
    numbers = numbers[:]
    step = 0
    pos = 0
    step_no = 0
    while 0 <= pos < len(numbers):
        step = numbers[pos]
        numbers[pos] += 1
        step_no += 1
        pos += step
    return step_no

def main2(numbers):
    numbers = numbers[:]
    step = 0
    pos = 0
    step_no = 0
    while 0 <= pos < len(numbers):
        step = numbers[pos]
        numbers[pos] += 1 if numbers[pos] < 3 else -1
        step_no += 1
        pos += step
    return step_no

if __name__ == '__main__':
    with open('d5/input.txt', 'r') as fp:
        contents = [int(l.strip()) for l in fp.readlines()]
    print('1: ', main1(contents))
    print('2: ', main2(contents))
