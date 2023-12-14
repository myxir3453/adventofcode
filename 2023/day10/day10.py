import queue

with open('input', 'r') as fin:
    lines = [line.rstrip() for line in fin.readlines()]

nodes = [[None for x in range(len(lines))] for y in range(len(lines))]
snode = None
for y in range(len(lines)):
    for x in range(len(lines[y])):
        ch = lines[y][x]
        if ch == 'S':
            snode = ((y, x), [])
            nodes[y][x] = snode
        elif ch == '|':
            nodes[y][x] = ((y, x), [(y - 1, x), (y + 1, x)])
        elif ch == '-':
            nodes[y][x] = ((y, x), [(y, x - 1), (y, x + 1)])
        elif ch == 'L':
            nodes[y][x] = ((y, x), [(y - 1, x), (y, x + 1)])
        elif ch == 'J':
            nodes[y][x] = ((y, x), [(y - 1, x), (y, x - 1)])
        elif ch == '7':
            nodes[y][x] = ((y, x), [(y, x - 1), (y + 1, x)])
        elif ch == 'F':
            nodes[y][x] = ((y, x), [(y, x + 1), (y + 1, x)])
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if nodes[y][x] != None \
            and snode != None \
            and snode[0] in nodes[y][x][1]:
            snode[1].append((y, x))

print(snode)

q = queue.Queue()
dist = [[None for x in range(len(lines))] for y in range(len(lines))]
dist[snode[0][0]][snode[0][1]] = 0
q.put(snode)
lc = 0
while not q.empty():
    node = q.get()
    for nbor in node[1]:
        if dist[nbor[0]][nbor[1]] == None:
            dist[nbor[0]][nbor[1]] = dist[node[0][0]][node[0][1]] + 1
            q.put(nodes[nbor[0]][nbor[1]])

farthest = 0
for y in range(len(dist)):
    for x in range(len(dist[y])):
        if dist[y][x] != None and farthest < dist[y][x]:
            farthest = dist[y][x]
print(farthest)
