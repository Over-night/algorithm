class loc:
    def __init__(self, row, col):
        self._row = row
        self._col = col

    def move(self, loc):
        self._row += loc._row
        self._col += loc._col



map_size = int(input())

DIR = [
    loc(0,-1),
    loc(1,0),
    loc(0,1),
    loc(-1,0)
]

tornado_loc = loc(map_size//2,map_size//2)

weight_max = map_size * 2 - 2
for weight in range(weight_max):
    move_count = 1 + weight // 2
    move_dir = weight % 4

    for cnt in range(move_count):
        tornado_loc.move(DIR[move_dir])
        # 대충 모래 이동 로직 


    