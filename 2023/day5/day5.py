import math
import queue
#import pdb; pdb.set_trace()

fileName = 'input'

def read_next_map(fin):
    fin.readline()
    mapping = []
    keep_reading = True
    while keep_reading:
        line = fin.readline()
        splitted = line.split()
        if len(splitted) == 0:
            keep_reading = False
        else:
            destination_start = int(splitted[0])
            source_start = int(splitted[1])
            range_length = int(splitted[2])
            mapping.append({
                'source_range': range(source_start, source_start + range_length),
                'destination_range': range(destination_start, destination_start + range_length)
                })
    return mapping

def map_number(number, source_range, destination_range):
    return destination_range[0] + number - source_range[0]

def get_ranges_intersection(x, y):
    intersection = range(max(x.start, y.start), min(x.stop, y.stop))
    if len(intersection) == 0:
        return None
    return intersection

def get_difference(x, y):
    intersection = get_ranges_intersection(x, y)

    if intersection == None:
        return [x]

    i = intersection[0]
    j = intersection[-1]

    if y[0] <= x[0] and y[-1] >= x[-1]:
        return []
    if y[0] <= x[0] and y[-1] < x[-1]:
        return [range(j + 1, x.stop)]
    if y[0] > x[0] and y[-1] < x[-1]:
        return [range(x.start, i), range(j + 1, x.stop)]
    if y[0] > x[0] and y[-1] >= x[-1]:
        return [range(x.start, i)]

def map_range(x, source_range, destination_range):
    y = source_range

    intersection = get_ranges_intersection(x, y)
    
    if intersection == None:
        return []
    if intersection == x:
        return [range(map_number(x.start, source_range, destination_range), \
                      map_number(x.stop, source_range, destination_range))]
    
    i = intersection[0]
    j = intersection[-1]

    if y[0] <= x[0] and y[-1] < x[-1]:
        # return map_range(range(x.start, j + 1), source_range, destination_range) + [range(j + 1, x.stop)]
        return map_range(range(x.start, j + 1), source_range, destination_range)
    if y[0] > x[0] and y[-1] < x[-1]:
        # return [range(x.start, i)] + map_range(y, source_range, destination_range) + [range(j + 1, x.stop)]
        return map_range(y, source_range, destination_range)
    if y[0] > x[0] and y[-1] >= x[-1]:
        # return [range(x.start, i)] + map_range(range(i, x.stop), source_range, destination_range) 
        return map_range(range(i, x.stop), source_range, destination_range) 

# tests
assert get_difference(range(10, 20), range(0, 5)) == [range(10, 20)]
assert get_difference(range(10, 20), range(0, 11)) == [range(11, 20)]
assert get_difference(range(10, 20), range(0, 15)) == [range(15, 20)]
assert get_difference(range(10, 20), range(10, 15)) == [range(15, 20)]
assert get_difference(range(10, 20), range(14, 17)) == [range(10, 14), range(17, 20)]
assert get_difference(range(10, 20), range(14, 20)) == [range(10, 14)]
assert get_difference(range(10, 20), range(14, 25)) == [range(10, 14)]
assert get_difference(range(10, 20), range(19, 25)) == [range(10, 19)]
assert get_difference(range(10, 20), range(5, 25)) == []
assert get_difference(range(81, 95), range(25, 95)) == []

# assert map_range(range(10, 20), range(0, 5), range(100, 105)) == [range(10, 20)]
# assert map_range(range(10, 20), range(0, 11), range(100, 111)) == [range(110, 111), range(11, 20)]
# assert map_range(range(10, 20), range(0, 15), range(100, 115)) == [range(110, 115), range(15, 20)]
# assert map_range(range(10, 20), range(10, 15), range(110, 115)) == [range(110, 115), range(15, 20)]
# assert map_range(range(10, 20), range(14, 17), range(114, 117)) == [range(10, 14), range(114, 117), range(17, 20)]
# assert map_range(range(10, 20), range(14, 20), range(114, 120)) == [range(10, 14), range(114, 120)]
# assert map_range(range(10, 20), range(14, 25), range(114, 125)) == [range(10, 14), range(114, 120)]
# assert map_range(range(10, 20), range(19, 25), range(119, 125)) == [range(10, 19), range(119, 120)]

assert map_range(range(10, 20), range(0, 5), range(100, 105)) == []
assert map_range(range(10, 20), range(0, 11), range(100, 111)) == [range(110, 111)]
assert map_range(range(10, 20), range(0, 15), range(100, 115)) == [range(110, 115)]
assert map_range(range(10, 20), range(10, 15), range(110, 115)) == [range(110, 115)]
assert map_range(range(10, 20), range(14, 17), range(114, 117)) == [range(114, 117)]
assert map_range(range(10, 20), range(14, 20), range(114, 120)) == [range(114, 120)]
assert map_range(range(10, 20), range(14, 25), range(114, 125)) == [range(114, 120)]
assert map_range(range(10, 20), range(19, 25), range(119, 125)) == [range(119, 120)]
assert map_range(range(10, 20), range(5, 25), range(105, 125)) == [range(110, 120)]

all_maps = []
with open(fileName, 'r') as fin:
    line = fin.readline()
    seeds = [int(x) for x in line[len("seeds: "):].split()]
    fin.readline()
    all_maps = [read_next_map(fin) for i in range(0, 7)]

min_location = 1 << 32

for i in range(0, int(len(seeds) / 2)):
    seed_range = range(seeds[i * 2], seeds[i * 2] + seeds[i * 2 + 1])
    mapped = [seed_range]
    unmapped = []

    #print(mapped)
    map_index = 0

    for map in all_maps:
        #print('new map')
        unmapped += [x for x in mapped]
        mapped = []

        pair_index = 0

        for pair in map:
            source_range = pair['source_range']
            destination_range = pair['destination_range']

            to_add = []
            for range_index in range(len(unmapped)):
                mapped += map_range(unmapped[range_index], source_range, destination_range)
                difference = get_difference(unmapped[range_index], source_range)
                if len(difference) == 0:
                    unmapped[range_index] = None
                if len(difference) > 0:
                    unmapped[range_index] = difference[0]
                if len(difference) > 1:
                    to_add += difference[1:]
            while None in unmapped:
                unmapped.remove(None)
            unmapped += to_add

            #print('unmapped: ' + str(unmapped), 'mapped: ' + str(mapped))

    for r in unmapped:
        if r.start < min_location:
            min_location = r.start
    for r in mapped:
        if r.start < min_location:
            min_location = r.start

print(min_location)
