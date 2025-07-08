MOVE_DIR = [
    [-1, 0],
    [-1, 1],
    [0, 1],
    [1, 1],
    [1, 0],
    [1, -1],
    [0, -1],
    [-1, -1]
]

class Fireball:
    def __init__(self, row, col, mass, speed, direction):
        self._row = row
        self._col = col
        self._mass = mass
        self._speed = speed
        self._direction = direction

    def move(self):
        self._row += MOVE_DIR[self._direction][0] * self._speed
        self._col += MOVE_DIR[self._direction][1] * self._speed
        self._row = (self._row-1) % size_board + 1 if self._row > 0 else size_board - (-1 * self._row) % size_board
        self._col = (self._col-1) % size_board + 1 if self._col > 0 else size_board - (-1 * self._col) % size_board
     
    def __str__(self):
        return f'({self._row} , {self._col})\nm : {self._mass} | s : {self._speed} | d : {self._direction}'

def combine_fireballs(fireballs):
    mass_sum = 0
    speed_sum = 0

    for fireball in fireballs:
        mass_sum += fireball._mass
        speed_sum += fireball._speed


    dir_new = fireballs[0]._direction % 2
    for i in range(1, len(fireballs)):
        if fireballs[i]._direction % 2 != dir_new:
            return mass_sum // 5, speed_sum // len(fireballs), 1
    
    return mass_sum // 5 , speed_sum // len(fireballs), 0


size_board, count_fireball, count_order = map(int, input().split())

list_fireballs = []
for _ in range(count_fireball):
    # row, col, mass, speed, direction = map(int, input().split())
    list_fireballs.append(Fireball(*map(int, input().split())))

for _ in range(count_order):
    pos_map = {}

    for fireball in list_fireballs:
        fireball.move()
        pos = (fireball._row, fireball._col)

        if pos in pos_map:
            pos_map[pos].append(fireball)
        else:
            pos_map[pos] = [fireball]

    # 2
    list_fireballs_new = []
    for pos, fireballs in pos_map.items():

        if len(fireballs) <= 0:
            continue
    
        if len(fireballs) == 1:
            list_fireballs_new.append(fireballs[0])
        else:
            new_mass, new_speed, new_dir = combine_fireballs(fireballs)
            if new_mass <= 0:
                continue
            for weight in range(4):
                list_fireballs_new.append(Fireball(*pos, new_mass, new_speed, new_dir + 2 * weight))
    
    list_fireballs = list_fireballs_new

sum_mass = 0
for fireball in list_fireballs:
    sum_mass += fireball._mass

print(sum_mass)