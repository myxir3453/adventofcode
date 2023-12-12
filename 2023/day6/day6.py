import re
import math

lines = []
with open('testinput', 'r') as fin:
    lines = fin.readlines()

race_times = [int(x) for x in re.findall("[0-9]+", lines[0])]
race_distances = [int(x) for x in re.findall("[0-9]+", lines[1])]

nr_races = len(race_times)

part1 = 1

for i in range(nr_races):
    rt = race_times[i]
    rd = race_distances[i]

    x1 = (-rt + math.sqrt(rt ** 2 - 4 * rd)) / (-2)
    x2 = (-rt - math.sqrt(rt ** 2 - 4 * rd)) / (-2)

    first_good_value = math.ceil(x1) if x1 != math.ceil(x1) else int(x1 + 1)
    last_good_value = math.floor(x2) if x2 != math.floor(x2) else int(x2 - 1)
    
    nr_solutions = last_good_value - first_good_value + 1

    part1 *= nr_solutions

print(part1)
