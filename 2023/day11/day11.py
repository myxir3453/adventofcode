import re
import queue

with open('input', 'r') as fin:
    lines = [line.rstrip() for line in fin.readlines()]

height = len(lines)
width = len(lines[0])

empty_rows = [row for row in range(height)
    if set([ch for ch in lines[row]]) == {'.'}]
empty_cols = [col for col in range(width)
    if set([lines[row][col] for row in range(height)]) == {'.'}]
costs = [[1 for col in range(width)] for row in range(height)]
for row in empty_rows:
    for col in range(width):
        costs[row][col] = 2
for col in empty_cols:
    for row in range(height):
        costs[row][col] = 2

gals = []
for row in range(height):
    matches = re.finditer(r"(\#)", lines[row])
    for match in matches:
        gals.append((row, match.start()))

sumdist = 0

for gal1id in range(len(gals) - 1):
    gal1 = gals[gal1id]
    dist = [[None for col in range(width)] for row in range(height)]
    dist[gal1[0]][gal1[1]] = 0
    q = queue.Queue()
    q.put(gal1)
    while not q.empty():
        v = q.get()
        nbors = []
        if v[0] > 0:
            nbors.append((v[0] - 1, v[1]))
        if v[0] < width - 1:
            nbors.append((v[0] + 1, v[1]))
        if v[1] > 0:
            nbors.append((v[0], v[1] - 1))
        if v[1] < height - 1:
            nbors.append((v[0], v[1] + 1))
        for nbor in nbors:
            if dist[nbor[0]][nbor[1]] == None:
                newdist = dist[v[0]][v[1]] + costs[v[0]][v[1]]
                dist[nbor[0]][nbor[1]] = newdist
                q.put(nbor)

    # for row in range(height):
    #     print([str(dist[row][col]).rjust(5) for col in range(width)])

    for gal2id in range(gal1id + 1, len(gals)):
        gal2 = gals[gal2id]
        sumdist += dist[gal2[0]][gal2[1]]

print(sumdist)
