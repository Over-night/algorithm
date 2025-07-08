city_amount = int(input())
city_map = [list(map(int, input().split())) for _ in range(city_amount)]

dp = [[2147483647 for _ in range(city_amount)] for _ in range(1<<city_amount)]
dp[1][0] = 0 # 0->0

# 모든 경우 확인 / 비트마스크로 현황 확인 
for visited in range(1<<city_amount):
    # 이전 방문도시
    for before in range(city_amount):
        # 현재 경우에서 이전 방문도시가 포함안될 경우 pass
        if not (visited & (1<<before)):
            continue
        # 다음 방문 도시
        for next in range(city_amount):
            # 방문했을경우 건너뜀
            if visited & (1<<next): 
                continue
            # 불가능한 경로일 경우
            if city_map[before][next] == 0:
                continue
            dp[visited | (1<<next)][next] = min(dp[visited | (1<<next)][next], dp[visited][before] + city_map[before][next])

result = min(dp[(1<<city_amount) - 1][idx] + city_map[idx][0] if city_map[idx][0] > 0 else 2147483647 for idx in range(city_amount)) # 모든도시 방문한 경우에 대한 탐색
print(result)

# def search(city_map, chk, now, cost, info_map):
#     chk[now] = 1
#     chk[-1] += 1
    
#     if chk[-1] == len(city_map):
#         cost += city_map[now][info_map[1]]
#         if city_map[now][info_map[1]] > 0 and cost < info_map[0]:
#             info_map[0] = cost
        
#         chk[now] = 0
#         chk[-1] -= 1
#         return
#     if cost >= info_map[0]:
#         chk[now] = 0
#         chk[-1] -= 1
#         return

#     for idx in range(city_amount):
#         if city_map[now][idx] == 0 or chk[idx] > 0:
#             continue
        
#         search(city_map, chk, idx, cost+city_map[now][idx], info_map)

#     chk[now] = 0
#     chk[-1] -= 1


# city_amount = int(input())
# city_map = [list(map(int, input().split())) for _ in range(city_amount)]

# info_map = [2147483647, -1]
# for st in range(city_amount):
#     chk = [0 for _ in range(city_amount + 1)]
#     now = st
#     info_map[1] = st

#     search(city_map, chk, now, 0, info_map)


# print(info_map[0]) 