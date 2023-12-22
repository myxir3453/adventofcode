with open('input', 'r') as fin:
    lines = [line.rstrip() for line in fin.readlines()]

nrows = len(lines)
ncols = len(lines[0])
values = [[0 for x in range(ncols)] for y in range(nrows)]

rrocks = []

for y in range(nrows):
    for x in range(ncols):
        if lines[y][x] == '#':
            values[y][x] = None
        elif lines[y][x] == 'O':
            rrocks.append((y, x))

for x in range(ncols):
    if lines[0][x] != '#':
        values[0][x] = nrows

for y in range(1, nrows):
    for x in range(ncols):
        if lines[y][x] == '#':
            continue
        if lines[y - 1][x] == 'O':
            values[y][x] = values[y - 1][x] - 1
        elif lines[y - 1][x] == '#':
            values[y][x] = nrows - y
        else:
            values[y][x] = values[y-1][x]

total = 0
for rrock in rrocks:
    total += values[rrock[0]][rrock[1]]
print(total)

# for y in range(nrows):
#     print([str(value).rjust(4, ' ') for value in values[y]])
