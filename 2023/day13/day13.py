import functools

def to_binary(pattern : list[str]):
    return [int(''.join(map(lambda ch:'1' if ch=='#' else '0', line)), base=2)
            for line in pattern]

def get_mirror_index(pattern : list[str], can_be_off_by_one : bool) -> int:
    binpat = to_binary(pattern)

    # for nr in binpat:
    #     print(bin(nr)[2:].rjust(len(pattern[0]), '0') + ' - ' + str(nr))

    for i in range(1, len(binpat)):
        pairs = [(l, r) for (l, r) in zip(binpat[i - 1::-1], binpat[i:])]
        # print(pairs)
        diffs = [abs(l - r) for (l, r) in pairs if abs(l - r) > 0]
        # print(diffs)

        if diffs == []:
            return i
        if can_be_off_by_one and len(diffs) == 1:
            diff = diffs[0]
            if diff & (diff - 1) == 0:
                return i
    return 0

patterns = [[]]
with open('testinput', 'r') as fin:
    for line in fin:
        line = line.rstrip()

        if line != '':
            patterns[-1].append(line)
        else:
            patterns.append([])

total_part1 = 0
total_part2 = 0
for pattern in patterns:
    # print('find horizontal line of reflection')
    ahz = get_mirror_index(pattern, 0)
    if ahz != 0:
        # print(ahz)
        total_part1 += ahz * 100
    else:
        # print('fix smudge for horizontal line of reflection')
        ahz = get_mirror_index(pattern, 1)
        # print(ahz)
        total_part2 += ahz * 100

    # print('find vertical line of reflection')
    rotated = []
    for x in range(len(pattern[0])):
        row = ""
        for y in range(len(pattern)):
            row += pattern[y][x]
        rotated.append(row)
    ltv = get_mirror_index(rotated, 0)
    if ltv != 0:
        # print(ltv)
        total_part1 += ltv
    else:
        # print('fix smudge for vertical line of reflection')
        ltv = get_mirror_index(rotated, 1)
        # print(ltv)
        total_part2 += ltv

    # print()

print(total_part1)
print(total_part2)
