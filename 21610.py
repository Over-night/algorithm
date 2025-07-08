map_size, task_count = map(int, input().split())
map_info = [list(map(int, input().split())) for _ in range(map_size)]

class Locate:
    def __init__(self, row, col):
        self._row = row
        self._col = col

    def move_locate(self, loc, magnification, map_size):
        self._row += loc._row * magnification
        self._col += loc._col * magnification
        
        # 범위조절
        while self._row >= map_size: 
            self._row -= map_size
        while self._col >= map_size: 
            self._col -= map_size
        while self._row < 0: 
            self._row += map_size
        while self._col < 0: 
            self._col += map_size

cloud_list = [
    Locate(row=map_size-1,col=0), 
    Locate(row=map_size-1,col=1), 
    Locate(row=map_size-2,col=0), 
    Locate(row=map_size-2,col=1)
]
cloud_check = [[0 for _ in range(map_size)] for _ in range(map_size)]
for cloud in cloud_list:
        cloud_check[cloud._row][cloud._col] = 1
        
direction_all = [
    Locate(row=0,col=-1),
    Locate(row=-1,col=-1),
    Locate(row=-1,col=0),
    Locate(row=-1,col=1),
    Locate(row=0,col=1),
    Locate(row=1,col=1),
    Locate(row=1,col=0),
    Locate(row=1,col=-1)
]
direction_diagonal = [
    Locate(row=-1,col=-1),
    Locate(row=-1,col=1),
    Locate(row=1,col=1),
    Locate(row=1,col=-1)
]

for tr in range(0, task_count):
    direction, distance = map(int, input().split())
    
    # 1~2. 구름 이동 & 물량 증가
    for cloud in cloud_list:
        cloud_check[cloud._row][cloud._col] -= 1
        cloud.move_locate(direction_all[direction-1], distance, map_size)
        map_info[cloud._row][cloud._col] += 1
        cloud_check[cloud._row][cloud._col] += 1
    
    
    # 4. 물이 복사가 된다고~
    for cloud in cloud_list:
        # 대각선 확인
        for diagonal in direction_diagonal:
            row_chk = cloud._row + diagonal._row
            col_chk = cloud._col + diagonal._col
            if row_chk < 0 or col_chk < 0 or row_chk >= map_size or col_chk >= map_size:
                continue
            
            # 물이 있으면 복사
            map_info[cloud._row][cloud._col] += 1 if map_info[row_chk][col_chk] > 0 else 0
    
    new_cloud_list = []        
    for r in range(map_size):
        for c in range(map_size):
            if map_info[r][c] >= 2 and cloud_check[r][c] == 0:
                map_info[r][c] -= 2
                new_cloud_list.append(Locate(r, c))
                cloud_check[r][c] += 1
    

    # 3. 구름 삭제
    for old in cloud_list:
        cloud_check[old._row][old._col] -= 1
    del cloud_list
    cloud_list = new_cloud_list
            

# 결과
bucket_sum = 0
for row in map_info:
    for col in row:
        bucket_sum += col
        
print(bucket_sum)