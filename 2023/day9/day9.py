with open('input', 'r') as fin:
    lines = fin.readlines()

sum = 0

for line in lines:
    h = [int(x) for x in line.rstrip().split()]

    stack = []
    while any([x != 0 for x in h]):
        stack.append(h[0])
        for i in range(0, len(h) - 1):
            h[i] = h[i + 1] - h[i]
        
        h.pop(-1)

    p = stack.pop(-1)
    while len(stack) > 0:
        p = stack.pop(-1) - p
    
    sum += p

print(sum)
