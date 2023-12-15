import functools

def get_mirror_index(v):
    for i in range(1, len(v)):
        if not any([l != r for l, r in zip(v[i - 1::-1], v[i:])]):
            return i
    return 0

patterns = [[]]
with open('input', 'r') as fin:
    for line in fin:
        line = line.rstrip()
        if line != '':
            patterns[-1].append(line)
        else:
            patterns.append([])

total = 0
for pattern in patterns:
    print('find horizontal line of reflection')
    rows = []
    rowdic = {}
    cnum = 0
    for row in pattern:
        if row not in rowdic:
            cnum += 1
            rowdic[row] = cnum
        rows.append(rowdic[row])
    print(rows)
    ahz = get_mirror_index(rows)
    print(ahz)

    print('find vertical line of reflection')
    cols = []
    coldic = {}
    cnum = 0
    for x in range(len(pattern[0])):
        col = ''.join([pattern[y][x] for y in range(len(pattern))])
        if col not in coldic:
            cnum += 1
            coldic[col] = cnum
        cols.append(coldic[col])
    print(cols)
    ltv = get_mirror_index(cols)
    print(ltv)

    total += ahz * 100
    total += ltv

    print()

print('Total = ' + str(total))
