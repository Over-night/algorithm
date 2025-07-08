app_amount, memory_todecrease = map(int, input().split())
app_memory = list(map(int, input().split()))
app_cost = list(map(int, input().split()))
app_info = []

max_app_cost = 0
for idx in range(app_amount-1,-1,-1):
    if app_cost[idx] == 0:
        memory_todecrease -= app_memory[idx]
        app_cost.pop(idx)
        app_memory.pop(idx)
        continue
    max_app_cost += app_cost[idx]

if memory_todecrease <= 0:
    print(0)
    exit(0)

app_amount = len(app_cost)
dp = [0] + [0 for _ in range(max_app_cost)]

for idx in range(app_amount):
    for current_cost in range(max_app_cost, app_cost[idx]-1, -1):
        dp[current_cost] = max(dp[current_cost],dp[current_cost-app_cost[idx]] + app_memory[idx])

for cost, memory in enumerate(dp):
    if memory >= 1000000000 or memory <= 0:
        continue
    if memory >= memory_todecrease:
        print(cost)
        break



'''
앱은 '활성화' 보이지 않더라도 메인 메모리에 직전의 상태가 기록
메모리 부족을 해결하기 위해 앱을 '비활성화'
앱을 재실행할 경우 시간이 소요됨
비용을 최소화하자

30 3 
20 3 
35 5 
40 4 

10 0 @
30 3 10
20 3 6.x
40 4 10
35 5 7

2(10) + 
'''