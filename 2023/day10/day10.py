import queue
import math

with open('input', 'r') as fin:
    lines = [line.rstrip() for line in fin.readlines()]

nodes_matrix = [[None for x in range(len(lines[0]))] for y in range(len(lines))]
snode = None
for y in range(len(lines)):
    for x in range(len(lines[y])):
        ch = lines[y][x]
        if ch == 'S':
            snode = ((y, x), [])
            nodes_matrix[y][x] = snode
        elif ch == '|':
            nodes_matrix[y][x] = ((y, x), [(y - 1, x), (y + 1, x)])
        elif ch == '-':
            nodes_matrix[y][x] = ((y, x), [(y, x - 1), (y, x + 1)])
        elif ch == 'L':
            nodes_matrix[y][x] = ((y, x), [(y - 1, x), (y, x + 1)])
        elif ch == 'J':
            nodes_matrix[y][x] = ((y, x), [(y - 1, x), (y, x - 1)])
        elif ch == '7':
            nodes_matrix[y][x] = ((y, x), [(y, x - 1), (y + 1, x)])
        elif ch == 'F':
            nodes_matrix[y][x] = ((y, x), [(y, x + 1), (y + 1, x)])
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if nodes_matrix[y][x] != None \
            and snode != None \
            and snode[0] in nodes_matrix[y][x][1]:
            snode[1].append((y, x))

# for y in range(len(lines)):
#     for x in range(len(lines[y])):
#         if nodes_matrix[y][x] == None:
#             print('□', end='')
#         elif nodes_matrix[y][x] == snode:
#             print('■', end='')
#         else:
#             print('■', end='')
#     print()

q = queue.Queue()
dist = [[None for x in range(len(lines[y]))] for y in range(len(lines))]
dist[snode[0][0]][snode[0][1]] = 0
q.put(snode)
lc = 0
while not q.empty():
    node = q.get()
    for nbor in node[1]:
        if dist[nbor[0]][nbor[1]] == None:
            dist[nbor[0]][nbor[1]] = dist[node[0][0]][node[0][1]] + 1
            q.put(nodes_matrix[nbor[0]][nbor[1]])

farthest = 0
for y in range(len(dist)):
    for x in range(len(dist[y])):
        # print(str(dist[y][x]).rjust(5), end='')
        if dist[y][x] != None and farthest < dist[y][x]:
            farthest = dist[y][x]
    # print()
print(farthest)

path = []
stack = [snode]
done = False
while not done and len(stack) > 0:
    node = stack.pop()
    path.append(node[0])
    for nbor in node[1]:
        if nbor == snode:
            done = True
        elif nbor not in path:
            stack.append(nodes_matrix[nbor[0]][nbor[1]])

#print(len(path))

area = 0
for i in range(len(path)):
    nexti = i + 1 if i < len(path) - 1 else 0
    previ = i - 1 if i > 0 else len(path) - 1
    cnode = path[i]
    nextnode = path[nexti]
    prevnode = path[previ]
    area += cnode[0] * (nextnode[1] - prevnode[1])
area = int(math.floor(area / 2))
if area < 0:
    area *= -1

total_points = len(path)
points_inside = area - math.floor(total_points / 2) + 1

print(points_inside)
