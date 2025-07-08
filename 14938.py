INF = 999999999

loc_amount, find_range, road_amount = map(int, input().split())
map_item = list(map(int, input().split()))
map_road = [[] for _ in range(loc_amount)]
for _ in range(road_amount):
    pt1, pt2, cost = map(int, input().split())
    map_road[pt1-1].append([pt2-1, cost])
    map_road[pt2-1].append([pt1-1, cost])

loc_max = [0 for _ in range(loc_amount)]

for st in range(loc_amount):
    di = [INF for _ in range(loc_amount)]
    chk = [False for _ in range(loc_amount)]

    now = st
    di[now] = 0
    
    while now >= 0:
        for dest in map_road[now]:
            if chk[dest[0]]:
                continue
            to_cost = di[now] + dest[1]
            di[dest[0]] = di[dest[0]] if di[dest[0]] < to_cost else to_cost

        chk[now] = True
        min_distance = INF
        min_idx = -1
        for idx in range(loc_amount):
            if chk[idx]:
                continue
            if di[idx] < min_distance:
                min_idx = idx
                min_distance = di[idx]

        now = min_idx

    for idx in range(loc_amount):
        if di[idx] > find_range:
            continue
        loc_max[st] += map_item[idx]
    
print(max(loc_max))
    