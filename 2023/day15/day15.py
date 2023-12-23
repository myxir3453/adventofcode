def find_hash(string: str):
    val = 0
    for ch in list(string):
        val = ((val + ord(ch)) * 17) % 256
    return val

with open('input', 'r') as fin:
    line = fin.readline()

steps = line.split(',')
print(sum([find_hash(step) for step in steps]))
