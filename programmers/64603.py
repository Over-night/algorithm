import sys 
sys.setrecursionlimit(1000000)

def search(chk, pt):
    if pt not in chk:
        chk[pt] = pt
    elif chk[pt] != pt:
        chk[pt] = search(chk, chk[pt])
    return chk[pt]

def solution(k, room_number):
    answer = []
    chk = {}
    
    for num in room_number:
        # print(num, end = ' ')
        # 방 배정이 바로 가능한 경우
        if num not in chk:
            chk[num] = num + 1
            answer.append(num)
            continue
        
        # 방 배정이 바로 안되는 경우
        target = search(chk, num)
        answer.append(target)
        chk[target] = search(chk, target+1)
            
    return answer