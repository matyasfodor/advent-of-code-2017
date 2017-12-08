from collections import namedtuple, defaultdict

conditionals = {
    '>': lambda x, y: x > y,
    '<': lambda x, y: x < y,
    '>=': lambda x, y: x >= y,
    '<=': lambda x, y: x <= y,
    '!=': lambda x, y: x != y,
    '==': lambda x, y: x == y,
}

INCREMENT = 'inc'
DECREMENT = 'dec'

coefficient = {
    INCREMENT: 1,
    DECREMENT: -1,
}

Instruction = namedtuple('Instruction', 'register operation value condition')
Conditional = namedtuple('Conditional', 'operation register value')

def parse_instruction(line):
    register, operation, value, _, conditional_register, conditional_operation, conditional_value = line.split()
    conditional = Conditional(
        conditionals[conditional_operation],
        conditional_register,
        int(conditional_value)
    )
    return Instruction(register, operation, int(value), conditional)

def perform_instructions(instructions):
    regristry = defaultdict(lambda : 0)
    max_val = 0
    for line in instructions:
        instruction = parse_instruction(line)
        if instruction.condition.operation(regristry[instruction.condition.register], instruction.condition.value):
            regristry[instruction.register] += coefficient[instruction.operation] * instruction.value
            max_val = regristry[instruction.register] if regristry[instruction.register] > max_val else max_val
    return max(regristry.values()), max_val

def main1(instructions):
    return perform_instructions(instructions)[0]

def main2(instructions):
    return perform_instructions(instructions)[1]

if __name__ == '__main__':
    with open('d8/input.txt', 'r') as fp:
        contents = [l.strip() for l in fp.readlines()]
    print('1: ', main1(contents))
    print('2: ', main2(contents))
