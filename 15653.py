class Locate:
    def __init__(self, y, x):
        self._y = y
        self._x = x

n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]
stacks = [[None, None, 0]]
hole = None
for y in range(n):
    for x in range(m):
        if maps[y][x] == 'R':
            stacks[0][0] = Locate(y, x)
        if maps[y][x] == 'B':
            stacks[0][1] = Locate(y, x)
        if maps[y][x] == 'O':
            hole = Locate(y, x)
            

chk = [[[[0 for _ in range(n)] for _ in range(m)] for _ in range(n)] for _ in range(m)]
ed = -1

while len(stacks) > ed:
    ed += 1
    red, blue = stacks[ed][0], stacks[ed][1]
    
    

    