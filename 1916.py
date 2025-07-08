town_amount = int(input())
bus_amount = int(input())

len_town = town_amount + 1
town = [[] for _ in range(len_town)]

for _ in range(bus_amount):
    st, ed, cost = map(int, input().split())
    town[st].append([ed, cost])

orig, dest = map(int, input().split())

INF = 999999999999999
dp = [INF for _ in range(len_town)]
dp[orig] = 0
chk = [False for _ in range(len_town)]

while not chk[dest] :
    for line in town[orig]:
        cost = dp[orig] + line[1]
        if cost < dp[line[0]]:
            dp[line[0]] = cost
    
    chk[orig] = True
    min_val = INF
    min_idx = 0
    for idx in range(1, len_town):
        if chk[idx]:
            continue
        if dp[idx] < min_val:
            min_val = dp[idx]
            min_idx = idx
    
    orig = min_idx

    if min_idx == 0:
        break

print(dp[dest])