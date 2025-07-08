belt_size, limit_break = map(int, input().split())
belt_durability = list(map(int, input().split()))

LOC_UPPER = 0
LOC_LOWER = belt_size - 1
BELT_LENGTH = belt_size * 2

belt_status = [False for _ in range(BELT_LENGTH)]
robot_list = []

def get_locate(locate):
    global BELT_LENGTH

    return locate - 1 if locate > 0 else BELT_LENGTH - 1

def get_moveTo(locate):
    global BELT_LENGTH
    
    res = locate + 1
    
    return res if res < BELT_LENGTH else 0

step_count = 0
while limit_break > 0:
    step_count += 1
    
    # 1 : 벨트 이동
    LOC_UPPER = get_locate(LOC_UPPER)
    LOC_LOWER = get_locate(LOC_LOWER)
    # 로봇 제거 확인
    for i in range(len(robot_list)):
        if robot_list[i] == LOC_LOWER:
            belt_status[LOC_LOWER] = False
            robot_list.pop(i)
            break
    
    # 2 : 로봇 이동
    idx_lower = None
    for i in range(len(robot_list)):
        # 벨트가 비었다면 로봇 이동
        loc_moveTo = get_moveTo(robot_list[i])
        if belt_status[loc_moveTo] == False and belt_durability[loc_moveTo] > 0:
            belt_status[robot_list[i]] = False
            robot_list[i] = loc_moveTo
            belt_durability[loc_moveTo] -= 1
            if belt_durability[loc_moveTo] == 0:
                limit_break -= 1
            belt_status[loc_moveTo] = True
            if loc_moveTo == LOC_LOWER:
                idx_lower = i
    # 로봇 제거
    if idx_lower is not None:
        belt_status[robot_list[idx_lower]] = False
        robot_list.pop(idx_lower)
    
    # 3 : 로봇 올리기
    if belt_status[LOC_UPPER] == False and belt_durability[LOC_UPPER] > 0:
        belt_status[LOC_UPPER] = True
        belt_durability[LOC_UPPER] -= 1
        if belt_durability[LOC_UPPER] == 0:
            limit_break -= 1
        robot_list.append(LOC_UPPER)
        
print(step_count)