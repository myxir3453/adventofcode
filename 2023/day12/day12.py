import re

with open('input', 'r') as fin:
    lines = [line.rstrip() for line in fin.readlines()]

totalarr = 0

for lineidx in range(len(lines)):
    print('line ' + str(lineidx + 1) + ' / ' + str(len(lines)))
    line = lines[lineidx]
    record1 = line.split(' ')[0]
    record2 = [int(x) for x in line.split(' ')[1].split(',')]

    nr_screws = len(record1)

    record1 = record1.replace('.', '0')
    record1 = record1.replace('#', '1')
    # print(record1)

    masks_for_unknowns = []
    nr_unknowns = 0
    for un in re.finditer(r'(\?)', record1):
        mask = 2 ** (nr_screws - un.start(0) - 1)
        masks_for_unknowns.append(2 ** (nr_screws - un.start(0) - 1))
        nr_unknowns += 1
    masks_for_unknowns.reverse()
    # for mask in masks_for_unknowns:
    #     print(bin(mask)[2:].rjust(nr_screws, '0'))

    record1_base = int(record1.replace('?', '0'), base=2)
    # print(bin(record1)[2:].rjust(nr_screws, '0'))

    narr = 0

    # print()
    for k in range(2**nr_unknowns):
        #print(bin(k)[2:].rjust(nr_unknowns, '0'))

        record1 = record1_base
        for bit_index in range(nr_unknowns):
            #bit = (k & (1 << (nr_unknowns - bit_index - 1))) >> (nr_unknowns - bit_index - 1)
            bit = (k & (1 << bit_index)) >> bit_index
            #print(bit)
            if bit == 1:
                record1 |= masks_for_unknowns[bit_index]
        
        record1_binary = bin(record1)[2:].rjust(nr_screws, '0')
        
        occs = [len(occ) for occ in re.findall(r'1+', record1_binary)]

        if occs == record2:
            narr += 1

    #print(str(narr) + ' arrangements')
    totalarr += narr

print(totalarr)
