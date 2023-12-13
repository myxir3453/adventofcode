import re
#import queue

with open('input', 'r') as fin:
    lines = [line.rstrip() for line in fin.readlines()]

ions = [ion for ion in lines[0]]
node_indexes = {}

nodes = []
for i in range(2, len(lines)):
    match = re.search(r'([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)', lines[i])
    src = match.group(1)
    left = match.group(2)
    right = match.group(3)
    nodes.append((src, left, right))
    node_indexes[src] = i - 2
nodes = [(node[0], node_indexes[node[1]], node_indexes[node[2]]) for node in nodes]
#print(nodes)

nsteps = 0
cnode = nodes[node_indexes['AAA']]
cion = 0
while cnode[0] != 'ZZZ':
    # print('current node: ' + cnode[0])
    # print('next instruction: ' + ions[cion])

    if ions[cion] == 'R':
        cnode = nodes[cnode[2]]
    else:
        cnode = nodes[cnode[1]]

    if cion < len(ions) - 1:
        cion += 1
    else:
        cion = 0

    nsteps += 1
# print('current node: ' + cnode[0])

print('steps: ' + str(nsteps))
