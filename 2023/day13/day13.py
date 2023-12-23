# credits to HyperNeutrino: https://youtu.be/GYbjIvTQ_HA?si=i69WdgTa3_NICFqc

import functools

def rotate(pattern):
    rotated = []
    for x in range(len(pattern[0])):
        row = ""
        for y in range(len(pattern)):
            row += pattern[y][x]
        rotated.append(row)
    return rotated

def get_mirror_index(pattern : list[str]) -> int:
    for r in range(1, len(pattern)):
        above = pattern[:r][::-1]
        below = pattern[r:]
        
        above = above[:len(below)]
        below = below[:len(above)]

        if (sum(sum(0 if a == b else 1 for a, b in zip(ai, bi)) for ai, bi in zip(above, below))) == 1:
            return r

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
    midx = get_mirror_index(pattern)
    total += midx * 100

    midx = get_mirror_index(rotate(pattern))
    total += midx

print(total)
