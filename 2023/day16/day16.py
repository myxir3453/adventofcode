with open('input', 'r') as fin:
    grid = [list(line.rstrip()) for line in fin.readlines()]
nrows = len(grid)
ncols = len(grid[0])

def go_right(pos, stack):
    #visit((pos[0], pos[1] + 1), (0, 1))
    stack.append(((pos[0], pos[1] + 1), (0, 1)))
def go_left(pos, stack):
    #visit((pos[0], pos[1] - 1), (0, -1))
    stack.append(((pos[0], pos[1] - 1), (0, -1)))
def go_up(pos, stack):
    #visit((pos[0] - 1, pos[1]), (-1, 0))
    stack.append(((pos[0] - 1, pos[1]), (-1, 0)))
def go_down(pos, stack):
    #visit((pos[0] + 1, pos[1]), (1, 0))
    stack.append(((pos[0] + 1, pos[1]), (1, 0)))
def go_on(pos, dir, stack):
    #visit((pos[0] + dir[0], pos[1] + dir[1]), dir)
    stack.append(((pos[0] + dir[0], pos[1] + dir[1]), dir))
def solve(startpos, startdir):
    visited = set()
    stack = []
    stack.append((startpos, startdir))
    while len(stack) > 0:
        pos, dir = stack.pop()
        if pos[0] not in range(nrows) or \
        pos[1] not in range(ncols):
            continue
        encounter = grid[pos[0]][pos[1]]
        if (pos, dir) in visited:
            continue
        visited.add((pos, dir))
        # print((pos[0] + 1, pos[1] + 1), dir)
        if encounter == '.':
            go_on(pos, dir, stack)
        if encounter == '|':
            if dir == (0, 1) or dir == (0, -1):
                go_up(pos, stack)
                go_down(pos, stack)
            else:
                go_on(pos, dir, stack)
        if encounter == '-':
            if dir == (1, 0) or dir == (-1, 0):
                go_right(pos, stack)
                go_left(pos, stack)
            else:
                go_on(pos, dir, stack)
        if encounter == '/':
            if dir == (0, 1):
                go_up(pos, stack)
            if dir == (0, -1):
                go_down(pos, stack)
            if dir == (1, 0):
                go_left(pos, stack)
            if dir == (-1, 0):
                go_right(pos, stack)
        if encounter == '\\':
            if dir == (0, 1):
                go_down(pos, stack)
            if dir == (0, -1):
                go_up(pos, stack)
            if dir == (1, 0):
                go_right(pos, stack)
            if dir == (-1, 0):
                go_left(pos, stack)
    return len(set(pos for pos, dir in visited))

starts = []
for col in range(ncols):
    starts.append(((0, col), (1, 0)))
    starts.append(((nrows - 1, col), (-1, 0)))
for row in range(nrows):
    starts.append(((row, 0), (0, 1)))
    starts.append(((row, ncols-1), (0, -1)))

maxenergy = max([solve(spos, sdir) for spos, sdir in starts])
print(maxenergy)

# grid2 = [['.' for col in range(ncols)] for row in range(nrows)]
# for pos, dir in visited:
#     print(pos)
#     grid2[pos[0]][pos[1]] = '#'
# [print(''.join(line)) for line in grid2]
