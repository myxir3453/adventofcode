fileName = 'input'

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
            mapping.append({
                'destinationRangeStart': int(splitted[0]),
                'sourceRangeStart': int(splitted[1]),
                'rangeLength': int(splitted[2])})
    return mapping

def apply_mapping(value, mapping):
    for pair in mapping:
        destinationRangeStart = pair['destinationRangeStart']
        sourceRangeStart = pair['sourceRangeStart']
        rangeLength = pair['rangeLength']
        if value >= sourceRangeStart and \
           value < sourceRangeStart + rangeLength:
            return destinationRangeStart + (value - sourceRangeStart)
    return value

with open(fileName, 'r') as fin:
    line = fin.readline()
    seeds = [int(x) for x in line[len("seeds: "):].split()]
    fin.readline()
    #print(seeds)

    mapped = [x for x in seeds]
    for i in range(7):
        mapping = read_next_mapping()
        mapped = [apply_mapping(x, mapping) for x in mapped]
        #print(mapped)
    
    print(min(mapped))
