with open('input', 'r') as fin:
    lines = fin.readlines()

p = 0

for line in lines:
    h = [int(x) for x in line.rstrip().split()]
    step = 0
    while any([x != 0 for x in h]):
        # print(h)

        p += h[-1]

        for i in range(len(h) - 1, 0, -1):
            h[i] -= h[i-1]
        
        h.pop(0)

        step += 1
    # print(h)

print(p)
