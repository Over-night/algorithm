gear_info = []
for _ in range(4):
    gear_info.append(list(input()))
gear_bias = [0 for _ in range(4)]

def getIndex(index, bias):
    res = index + bias
    if res > 7:
        res -= 8
    if res < 0:
        res += 8
    return res

task_count = int(input())
for _ in range(task_count):
    task_locate, task_direction = map(int, input().split())
    task_locate -= 1
    
    # 왼쪽 톱니바퀴 회전
    left_count = task_locate
    for i in range(task_locate, 0, -1):
        # 맞물린 바퀴의 극이 같을 경우 제외
        if gear_info[i][getIndex(gear_bias[i], -2)] == gear_info[i-1][getIndex(gear_bias[i-1], 2)]:
            break
        left_count -= 1

    # 오른쪽 톱니바퀴 회전
    right_count = task_locate
    for i in range(task_locate, 3):
        # 맞물린 바퀴의 극이 같을 경우 제외
        if gear_info[i][getIndex(gear_bias[i], 2)] == gear_info[i+1][getIndex(gear_bias[i+1], -2)]:
            break
        right_count += 1

    # 회전 처리
    direction = task_direction
    for i in range(task_locate - 1, left_count - 1, -1):
        gear_bias[i] = getIndex(gear_bias[i], direction)
        direction *= -1
    direction = task_direction
    for i in range(task_locate + 1, right_count + 1):
        gear_bias[i] = getIndex(gear_bias[i], direction)  
        direction *= -1
    gear_bias[task_locate] = getIndex(gear_bias[task_locate], -task_direction)
    
point = 0
for i in range(4):
    point += pow(2, i) * int(gear_info[i][gear_bias[i]])
    
print(point)