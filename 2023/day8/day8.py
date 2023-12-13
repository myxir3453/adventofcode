import re
from functools import reduce

def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmm(args):
    return reduce(lcm, args)

with open('input', 'r') as fin:
    lines = [line.rstrip() for line in fin.readlines()]

ions = [ion for ion in lines[0]]
node_indexes = {}

nodes = []
starting_nodes = []
ending_nodes = []
for i in range(2, len(lines)):
    # print(lines[i])
    match = re.search(r'([A-Z0-9]+) = \(([A-Z0-9]+), ([A-Z0-9]+)\)', lines[i])
    src = match.group(1)
    left = match.group(2)
    right = match.group(3)
    nodes.append((src, left, right))
    node_indexes[src] = i - 2
    if src[-1] == 'A':
        starting_nodes.append(i - 2)
    if src[-1] == 'Z':
        ending_nodes.append(i - 2)
nodes = [(node[0], node_indexes[node[1]], node_indexes[node[2]]) for node in nodes]
# print(nodes)

nstepsm = []
for starting_node in starting_nodes:
    nsteps = 0
    cnode = nodes[starting_node]
    # print('starting node: ' + cnode[0])
    cion = 0
    while cnode[0][-1] != 'Z':
        # print('current nodes: ' + str(cnodes))
        # print('next instruction: ' + ions[cion])

        if ions[cion] == 'R':
            cnode = nodes[cnode[2]]
        else:
            cnode = nodes[cnode[1]]

        nsteps += 1

        if cion < len(ions) - 1:
            cion += 1
        else:
            cion = 0
    # print('current nodes: ' + str(cnodes))

    nstepsm.append(nsteps)

print(lcmm(nstepsm))
