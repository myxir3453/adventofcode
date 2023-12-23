with open('input', 'r') as fin:
    grid = [list(line.rstrip()) for line in fin.readlines()]
nrows = len(grid)
ncols = len(grid[0])
visited = set()
stack = []

def go_right(pos):
    #visit((pos[0], pos[1] + 1), (0, 1))
    stack.append(((pos[0], pos[1] + 1), (0, 1)))
def go_left(pos):
    #visit((pos[0], pos[1] - 1), (0, -1))
    stack.append(((pos[0], pos[1] - 1), (0, -1)))
def go_up(pos):
    #visit((pos[0] - 1, pos[1]), (-1, 0))
    stack.append(((pos[0] - 1, pos[1]), (-1, 0)))
def go_down(pos):
    #visit((pos[0] + 1, pos[1]), (1, 0))
    stack.append(((pos[0] + 1, pos[1]), (1, 0)))
def go_on(pos, dir):
    #visit((pos[0] + dir[0], pos[1] + dir[1]), dir)
    stack.append(((pos[0] + dir[0], pos[1] + dir[1]), dir))

def solve(startpos, startdir):
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
            go_on(pos, dir)
        if encounter == '|':
            if dir == (0, 1) or dir == (0, -1):
                go_up(pos)
                go_down(pos)
            else:
                go_on(pos, dir)
        if encounter == '-':
            if dir == (1, 0) or dir == (-1, 0):
                go_right(pos)
                go_left(pos)
            else:
                go_on(pos, dir)
        if encounter == '/':
            if dir == (0, 1):
                go_up(pos)
            if dir == (0, -1):
                go_down(pos)
            if dir == (1, 0):
                go_left(pos)
            if dir == (-1, 0):
                go_right(pos)
        if encounter == '\\':
            if dir == (0, 1):
                go_down(pos)
            if dir == (0, -1):
                go_up(pos)
            if dir == (1, 0):
                go_right(pos)
            if dir == (-1, 0):
                go_left(pos)

solve((0, 0), (0, 1))

print(len(set(pos for pos, dir in visited)))

# grid2 = [['.' for col in range(ncols)] for row in range(nrows)]
# for pos, dir in visited:
#     print(pos)
#     grid2[pos[0]][pos[1]] = '#'
# [print(''.join(line)) for line in grid2]
