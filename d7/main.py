import re
from collections import namedtuple, defaultdict

Tower = namedtuple('Tower', 'name weigth children')
Tower.__hash__ = lambda self: hash(self.name)

def parse(line):
    line = line.split(' ')
    name = line[0]
    weigth = int(re.sub(r'[()]', '', line[1]))
    rest = ''.join(line[3:])
    children = rest.split(',') if rest else []
    return name, weigth, children

def root(towers):
    parents = {t[0] for t in towers}
    children = set()
    for t in towers:
        children.update(t[2])
    diff = (parents - children)
    assert len(diff) == 1
    return diff.pop()

def main1(lines):
    towers = [parse(l) for l in lines]
    return root(towers)

def outlier(children):
    if len(children) < 2:
        return None
    children = sorted(children)

    if children[0] == children[1] != children[-1]:
        return children[-1]
    elif children[0] == children[-1] != children[1]:
        return children[1]
    elif children[1] == children[-1] != children[0]:
        return children[0]
    else:
        return None

def main2(lines):
    towers = {Tower(*parse(l)) for l in lines}
    towers_by_name = {tower.name: tower for tower in towers}
    towers_total_weigth = {}
    for tower in towers:
        if len(tower.children) == 0:
            towers_total_weigth[tower.name] = tower.weigth
    while True:
        for tower in towers:
            weigth_by_children = {}
            children_by_weigth = defaultdict(list)
            for child in tower.children:
                if child in towers_total_weigth:
                    weigth_by_children[child] = towers_total_weigth[child]
                    children_by_weigth[towers_total_weigth[child]] = child

            if len(weigth_by_children) < len(tower.children):
                continue

            weigths = sorted(weigth_by_children.values())
            outlier_weigth = outlier(weigths)
            if outlier_weigth is not None:
                outlier_child = children_by_weigth[outlier_weigth]
                return towers_by_name[outlier_child].weigth - (outlier_weigth - weigths[1])
            else:
                towers_total_weigth[tower.name] = tower.weigth + sum(weigths)

if __name__ == '__main__':
    with open('d7/input.txt', 'r') as fp:
        lines = [l.strip() for l in fp.readlines()]
    print('1: ', main1(lines))
    print('1: ', main2(lines))
