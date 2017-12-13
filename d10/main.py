import operator
from functools import reduce
import binascii

def twist(string, pos, length):
    string = string[pos:] + string[:pos]
    string = list(reversed(string[:length])) + string[length:]
    return string[-pos:] + string[:-pos]

def round(instructions, string, pos=0, step_size=0):
    pos = 0
    for instruction in instructions:
        string = twist(string, pos, instruction)
        pos = (pos + instruction + step_size) % len(string)
        step_size += 1
    return string, pos, step_size

def main1(contents):
    instructions = [int(w) for w in contents.split(',')]
    string = list(range(256))
    string = round(instructions, string)[0]
    return string[0] * string[1]

def dense_hash(string):
    ret = []
    for i in range(0, 256, 16):
        ret.append(reduce(operator.xor, string[i: i + 16]))
    return ret

def hexa_convert(array):
    return ''.join('{0:02x}'.format(c) for c in array)

def main2(contents):
    instructions = [ord(c) for c in contents]
    instructions += [17, 31, 73, 47, 23]
    string = list(range(256))
    pos = 0
    step_size = 0
    for _ in range(64):
        string, pos, step_size = round(instructions, string, pos, step_size)
    print(step_size)
    dense = dense_hash(string)
    return hexa_convert(dense)

if __name__ == '__main__':
    with open('d10/input.txt', 'r') as fp:
        contents = fp.read().strip()
    print('1: ', main1(contents))
    print('2: ', main2(contents))
