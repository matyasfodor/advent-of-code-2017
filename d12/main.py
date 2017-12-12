def parse_line(l):
    splitted = l.split()
    origin = splitted[0]
    targets = splitted[2:]
    targets = ''.join(targets)
    return origin, targets.split(',')

def connections(nodes, starting_point):
    nodes_visited = set()
    nodes_to_visit = set()
    nodes_to_visit.update(nodes[starting_point])
    while nodes_to_visit:
        node = nodes_to_visit.pop()
        nodes_to_visit.update(set(nodes[node]) - nodes_visited)
        nodes_visited.add(node)
    return nodes_visited

def main1(rules):
    all_nodes = set()
    nodes = {}
    for rule in rules:
        source, targets = parse_line(rule)
        nodes[source] = targets
        all_nodes.add(source)
        all_nodes.update(targets)
    return len(connections(nodes, '0'))

def main2(rules):
    all_nodes = set()
    nodes = {}
    for rule in rules:
        source, targets = parse_line(rule)
        nodes[source] = targets
        all_nodes.add(source)
        all_nodes.update(targets)
    counter = 0
    while all_nodes:
        all_nodes -= connections(nodes, all_nodes.pop())
        counter += 1
    return counter

if __name__ == '__main__':
    with open('d12/input.txt', 'r') as fp:
        contents = [l.strip() for l in fp.readlines()]
    print('1: ', main1(contents))
    print('2: ', main2(contents))
