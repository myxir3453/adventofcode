with open('input', 'r') as fin:
    tiles = tuple([line.rstrip() for line in fin.readlines()])
    n = len(tiles)

def get_load(tiles):
    load = 0
    for row in range(n):
        load += tiles[row].count('O') * (n - row)
    return load

def run_cycle(tiles):
    for i in range(4):
        zipped = []
        for col in range(n):
            column = ''.join([tiles[row][col] for row in range(n)])
            splitted = column.split('#')
            splitted = [sorted(group, reverse=True) for group in splitted]
            splitted = [''.join(group) for group in splitted]
            joined = '#'.join(splitted)
            zipped.append(joined)
        tiles = list(zip(*zipped))
        tiles = tuple([
            ''.join([tiles[col][row] for col in range(n - 1, -1, -1)])
            for row in range(n)])
    return tiles

total_cycles = 1000000000
history_set = {tiles}
history = []
loads = []
for ncyc in range(total_cycles):
    tiles = run_cycle(tiles)
    load = get_load(tiles)
    if tiles in history_set:
        break
    else:
        history_set.add(tiles)
        history.append(tiles)
        loads.append(load)

cycle_start = history.index(tiles)
cycle_length = ncyc - cycle_start
print(cycle_start, cycle_length)

print(loads[(total_cycles - cycle_start) % cycle_length + cycle_start - 1])
