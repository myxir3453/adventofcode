import re

def hash(string: str):
    val = 0
    for ch in list(string):
        val = ((val + ord(ch)) * 17) % 256
    return val

def get_focusing_power(boxes):
    power = 0
    for boxnr, box in enumerate(boxes):
        for slot, lens in enumerate(box):
            for lenslbl in lens.keys():
                power += (1 + boxnr) * (1 + slot) * lens[lenslbl]
    return power

with open('input', 'r') as fin:
    line = fin.readline()

boxes = [[] for i in range(256)]
steps = line.split(',')
for step in steps:
    # print(step)
    match = re.search(r'([a-z]+)([=-])([0-9]?)', step)
    lenslbl = match.group(1)
    op = match.group(2)
    lenslen = int(match.group(3)) if op == '=' else None
    boxnr = hash(lenslbl)
    # print('box number: ' + str(boxnr))
    
    if op == '=':
        found = False
        for lens in boxes[boxnr]:
            if lenslbl in lens.keys():
                lens[lenslbl] = lenslen
                found = True
                break
        if not found:
            boxes[boxnr].append({lenslbl: lenslen})
    if op == '-':
        for lens in boxes[boxnr]:
            if lenslbl in lens.keys():
                boxes[boxnr].remove(lens)
                break
    
#     for i, box in enumerate(boxes):
#         if len(box) > 0:
#             print(i, box)
#     print()

# print('final state:')
# for i, box in enumerate(boxes):
#     if len(box) > 0:
#         print(i, box)
# print()

print(get_focusing_power(boxes))
