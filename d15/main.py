import re
from tqdm import tqdm

MULTIPLIERS = {
    'A': 16807,
    'B': 48271,
}

DIVISOR = 2147483647

def next_val(value, mutiplier, divisor):
    return (value * mutiplier) % divisor

def next_val_gen(value, mutiplier, divisor, divident):
    while True:
        value = (value * mutiplier) % divisor
        if value % divident == 0:
            yield value

def main1(values):
    A = values['A']
    B = values['B']
    counter = 0
    for _ in tqdm(range(int(40e6))):
        A = next_val(A, MULTIPLIERS['A'], DIVISOR)
        B = next_val(B, MULTIPLIERS['B'], DIVISOR)
        if '{0:016b}'.format(A)[-16:] == '{0:016b}'.format(B)[-16:]:
            counter += 1
    return counter

def main2(values):
    gen_A = next_val_gen(values['A'], MULTIPLIERS['A'], DIVISOR, 4)
    gen_B = next_val_gen(values['B'], MULTIPLIERS['B'], DIVISOR, 8)
    counter = 0
    for _ in tqdm(range(int(5e6))):
        if '{0:016b}'.format(next(gen_A))[-16:] == '{0:016b}'.format(next(gen_B))[-16:]:
            counter += 1
    return counter


MATCHER = re.compile(r'Generator (?P<name>[AB]) starts with (?P<number>[1-9][0-9]*)')
def parse_input(lines):
    ret = {}
    for line in lines:
        name, number = MATCHER.match(line).groups()
        ret[name] = int(number)
    return ret

if __name__ == '__main__':
    with open('d15/input.txt') as fp:
        values = parse_input(fp.readlines())
    print('1: ', main1(values))
    print('2: ', main2(values))
