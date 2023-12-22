with open('testinput', 'r') as fin:
    lines = [line.rstrip() for line in fin.readlines()]
    n = len(lines)

zipped = []
for col in range(n):
    column = ''.join([lines[row][col] for row in range(n)])
    splitted = column.split('#')
    splitted = [sorted(group, reverse=True) for group in splitted]
    splitted = [''.join(group) for group in splitted]
    joined = '#'.join(splitted)
    zipped.append(joined)
tiltednorth = list(zip(*zipped))
load = 0
for row in range(n):
    load += tiltednorth[row].count('O') * (n - row)
print(load)
