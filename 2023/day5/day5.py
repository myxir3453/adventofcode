import math

fileName = 'testinput'

def read_next_mapping():
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

def apply_mapping(value, mapping):
    for pair in mapping:
        destination_range = pair['destination_range']
        source_range = pair['source_range']
        if value in source_range:
            return destination_range[0] + (value - source_range[0])
    return value

def apply_mapping_to_range(r, mapping):
    # list of ranges
    result = []
    
    for pair in mapping:
        destination_range = pair['destination_range']
        source_range = pair['source_range']

        intmin = max([r[0], source_range[0]])
        intmax = min([r[-1], source_range[-1]])

        # no intersection, this mapping cannot transform any elements
        if intmin > intmax:
            continue
        
        mapped_intmin = min(destination_range) + intmin - min(source_range)
        mapped_intmax = min(destination_range) + intmax - min(source_range)

        # full intersection, this mapping can transform all elements
        if intmin == r[0] and intmax == r[-1]:
            result = [destination_range]
            break

        # intersection found
        if min(r) < min(source_range):
            result.append(range(min(r), intmin + 1))
            result.append(range(mapped_intmin, mapped_intmax + 1))
            result.append(range(intmax, max(source_range) + 1))
        if min(r) > min(source_range):
            result.append(range(mapped_intmin, mapped_intmax + 1))
            result.append(range(intmax, max(r) + 1))
        
    if len(result) == 0:
        result = [r]
    
    return result

with open(fileName, 'r') as fin:
    line = fin.readline()
    seeds = [int(x) for x in line[len("seeds: "):].split()]
    fin.readline()
    #print(seeds)

    all_mappings = []

    for i in range(7):
        mapping = read_next_mapping()
        all_mappings.append(mapping)
    
    # part 1
    min_location = 1 << 32
    for seed in seeds:
        v = seed
        for mapping in all_mappings:
            v = apply_mapping(v, mapping)
        if v < min_location:
            min_location = v
    
    #print(min_location)

    # part 2
    min_location = 1 << 32
    for i in range(0, math.floor(len(seeds) / 2)):
        ranges = [range(seeds[i * 2], seeds[i * 2] + seeds[i * 2 + 1])]
        for mapping in all_mappings:
            for r in ranges:
                results = apply_mapping_to_range(r, mapping)
                #print(results)
                for result in results:
                    ranges.append(result)
        if min_location > min([min(r) for r in ranges]):
            min_location = min([min(r) for r in ranges])
        
    #print(min_location)
