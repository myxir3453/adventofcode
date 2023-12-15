import re

cache = {}

def count_arrangements(record1, record2):
    # print((record1, record2))
    if record2 == ():
        return 1 if '#' not in record1 else 0
    
    res = 0
    
    # find first sliding window from record1 
    # that matches record2[0]; 
    # stop where rest of record1 would match with rest of record2
    swlen = record2[0]
    record2_remainder_length = sum(record2[1:]) + (len(record2) - 1)
    swend = len(record1) - swlen - record2_remainder_length

    for swstart in range(0, swend):
        window = record1[swstart : swstart + swlen]
        #print(((window, record1[swstart + swlen + 1:]), (record2[0], record2[1:])))
        if record1[swstart + swlen] == '#':
            continue
        if '#' in record1[:swstart]:
            break
        if '.' in window:
            continue
        nextargs = (record1[swstart + swlen + 1:], record2[1:])
        if nextargs not in cache:
            cache[nextargs] = count_arrangements(*nextargs)
        res += cache[nextargs]
    
    return res

with open('input', 'r') as fin:
    lines = [line.rstrip() for line in fin.readlines()]

total_arrangements = 0

for line in lines:
    record1, record2 = line.split()
    record2 = tuple(map(int, record2.split(',')))
    record2 = record2 * 5
    record1 = '?'.join([record1] * 5)
    record1 += '.'
    cache = {}
    total_arrangements += count_arrangements(record1, record2)

print(len(cache))
print(total_arrangements)
