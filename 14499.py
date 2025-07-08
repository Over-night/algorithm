class Loc:
    board_ver = 0
    board_hor = 0

    def __init__(self, row, col):
        self._row = row
        self._col = col
    def move(self, loc):
        tmp_row = self._row + loc._row
        tmp_col = self._col + loc._col
        if tmp_row < 0 or tmp_col < 0 or tmp_row >= self.board_ver or tmp_col >= self.board_hor:
            return False
        self._row = tmp_row
        self._col = tmp_col
        return True


'''
  1
3 0 2
  4
  5

  2
1 0 4
  3

0 : 3 2 4 1
1 : 3 2 0 5
2 : 0 5 4 1
3 : 5 0 4 1
4 : 3 2 5 0
5 : 2 3 4 1

0
'''
class Dice:
    move_to = [
        [3,2,4,1], # 0
        [3,2,0,5], # 1
        [0,5,4,1], # 2
        [5,0,4,1], # 3
        [3,2,5,0], # 4
        [2,3,4,1], # 5
    ]

    dir_to = [
        [0,1,2,3], # 정방향
        [3,2,1,0], # 
        [1,0,3,2], # 역방향 (180도)
        [2,3,0,1], # 
    ]

    def __init__(self):
        self._case = [0 for _ in range(6)]
        self._head = 0                          # 위를 바라보는 눈 인덱스
        self._dir = 0                           # 주사위 방향
        self._weight = [0,0]                    # 동서 / 남북

    def roll(self, order):
        order = order - 1
        self._weight[order//2] += 1
        # 회전 발생 시:
        if self._weight[0] > 0 and self._weight[1] > 0:
            self._head = self.move_to[self._head][self.dir_to[self._dir]]
            # dir 이동 로직

        
        return self._case[self._head]



board_ver, board_hor, loc_r, loc_c, order_count = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(board_ver)]
orders = list(map(int, input().split()))

loc = Loc(loc_r, loc_c)
Loc.board_ver = board_ver
Loc.board_hor = board_hor
dice = Dice()

direction = [
    None,
    Loc(0,1),
    Loc(0,-1),
    Loc(-1,0),
    Loc(1,0)
]


for order in orders:
    # 이동 
    if loc.move(direction[order]):
        continue
    
    print(dice.roll(order))


dir = [
    [4,3,5,2], # 1
    [4,3,1,6], # 2
    [1,6,5,2], # 3
    [6,1,5,2], # 4
    [4,3,6,1], # 5
    [3,4,5,2], # 6]
]
