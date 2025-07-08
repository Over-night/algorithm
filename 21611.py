map_size, blizard_count = map(int, input().split())
map_info = [list(map(int, input().split())) for _ in range(map_size)]

# * 방향 정보를 담는 클래스
class Locate:
    def __init__(self, y=0, x=0, loc=None):
        if loc == None:
            self._x = x
            self._y = y
        else:
            self._x = loc[1]
            self._y = loc[0]

    # 현재 위치에서 방향에 따라 한칸 이동
    def move(self, dir):
        if dir == 1:    # To Up
            self._y = self._y - 1
        elif dir == 2:  # To Down
            self._y = self._y + 1
        elif dir == 3:  # To Left
            self._x = self._x - 1
        elif dir == 4:  # To Right
            self._x = self._x + 1    
    def get(self):
        return self._y, self._x
            
            
# * 방향 카운팅 알고리즘
# 방향의 횟수
direction_order = [3,2,4,1]     # 방향의 순서 : 좌 하 우 상
direction_idx = 0
count = 1
direction_count = []
while count < map_size:
    direction_count.append(count)
    direction_count.append(count)
    count += 1
direction_count.append(direction_count[-1])

# 맵의 중앙 위치 구하기
distance_border = map_size // 2
location_center = Locate(y=distance_border, x=distance_border)


# * 순서 맵 구하기 
order_size = map_size * map_size - 1
map_order = [0 for _ in range(order_size)]
location_order = [[0 for _ in range(map_size)] for _ in range(map_size)] # 순서 맵
location_check = Locate(loc=location_center.get())
count = 0 

# 순서 맵 구하기 
for cnt in direction_count:
    for _ in range(cnt):
        location_check.move(direction_order[direction_idx])
        map_order[count] = map_info[location_check._y][location_check._x]
        location_order[location_check._y][location_check._x] = count
        count += 1
        
    # 확인 방향 전환 : 좌 하 우 상
    direction_idx += 1
    if direction_idx >= 4: 
        direction_idx = 0

ball_explode = [0 for _ in range(4)]  # 파괴된 구슬 카운팅

# * 구슬을 폭파하는 로직 
def explode():
    global map_order, ball_explode, order_size

    idx = -1
    idx_len = order_size - 1
    check_base = None # 기준점
    check_combo = 0
    check_idx = None
    is_explode = False
    
    while idx < idx_len:
        idx += 1
        
        # 빈 칸일 경우는 건너띔
        if map_order[idx] == 0: 
            continue
        
        # 이전 칸과 공이 같을 경우 : 콤보수 증가
        if check_base == None: 
            check_base = map_order[idx]
            check_combo += 1
            check_idx = idx
            continue
        elif map_order[idx] == check_base:
            check_combo += 1
            continue
        
        # 이전 칸과 공이 다를 경우 :
        # 폭발되지 않을 경우 계속
        if check_combo < 4:
            check_base = map_order[idx]
            check_combo = 1
            check_idx = idx
            continue
        
        # 폭발될 경우 공 제거
        is_explode = True
        ball_explode[check_base] += check_combo     # 공 폭발 개수 체크
        for i in range(check_idx, idx):
            map_order[i] = 0
            
        check_base = map_order[idx]
        check_combo = 1
        check_idx = idx

    # 콤보 확인 중 맵이 끝날 경우 체크
    if check_combo >= 4:
        is_explode = True
        ball_explode[check_base] += check_combo     # 공 폭발 개수 체크
        for i in range(check_idx, order_size):
            map_order[i] = 0

    return is_explode
    
# * 블리자드 마법 수행
for _ in range(blizard_count):
    direction, distance = map(int, input().split())

    # * 블리자드 마법을 이용한 구슬 파괴
    blizard_locate = Locate(loc=location_center.get())
    for _ in range(distance):
        blizard_locate.move(direction)
        map_order[location_order[blizard_locate._y][blizard_locate._x]] = 0
    
    # * 구슬을 폭파하는 로직 
    while explode():
        continue

    # * 구슬을 생성해 반영하는 로직
    idx = -1
    idx_len = order_size - 1
    check_base = None # 기준점
    check_combo = 0
    new_map_order = [0 for _ in range(order_size)]
    count = 0
    while idx < idx_len:
        idx += 1
        
        # 빈 칸일 경우는 건너띔
        if map_order[idx] == 0: 
            continue
        
        # 이전 칸과 공이 같을 경우 : 콤보수 증가
        if check_base == None:
            check_base = map_order[idx]
            check_combo = 1
            continue
        elif map_order[idx] == check_base:
            check_combo += 1
            continue
        
        # 연결된 구슬 개수 A, 연결된 구슬 종류 B가 있을때, 숫자 A B에 해당하는 구슬 삽입
        new_map_order[count] = check_combo
        new_map_order[count+1] = check_base
        count += 2
        if count >= order_size: # 새로 생성된 구슬이 맵 밖을 초과할 경우 : 추가 종료 
            break
        
        # 초기화
        check_base = map_order[idx]
        check_combo = 1
    
    if count < order_size and check_base is not None and check_base != 0:
        new_map_order[count] = check_combo
        new_map_order[count+1] = check_base
    
    # 맵 갱신
    del map_order
    map_order = new_map_order
    
    
# 답 계산
answer = 0
for i in range(1,4):
    answer += i * ball_explode[i]
print(answer)

