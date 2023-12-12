import re
import math
import functools

lines = []
with open('input', 'r') as fin:
    lines = fin.readlines()

race_times = [int(x) for x in re.findall("[0-9]+", lines[0])]
race_distances = [int(x) for x in re.findall("[0-9]+", lines[1])]

bigrace_time = int(functools.reduce(lambda x, y : x + y, re.findall("[0-9]+", lines[0])))
bigrace_distance = int(functools.reduce(lambda x, y : x + y, re.findall("[0-9]+", lines[1])))

def find_nr_race_solutions(rt, rd):
    x1 = (-rt + math.sqrt(rt ** 2 - 4 * rd)) / (-2)
    x2 = (-rt - math.sqrt(rt ** 2 - 4 * rd)) / (-2)

    first_good_value = math.ceil(x1) if x1 != math.ceil(x1) else int(x1 + 1)
    last_good_value = math.floor(x2) if x2 != math.floor(x2) else int(x2 - 1)
    
    nr_solutions = last_good_value - first_good_value + 1

    return nr_solutions

nr_races = len(race_times)

part1 = functools.reduce(
    lambda x, y : x * y,
    [find_nr_race_solutions(race_times[i], race_distances[i])
        for i in range(nr_races)])
print(part1)

part2 = find_nr_race_solutions(bigrace_time, bigrace_distance)
print(part2)
