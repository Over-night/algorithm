from collections import deque

case_amount = int(input())
    
while case_amount > 0:
    case_amount -= 1
    
    build_count, build_rule = map(int, input().split())
    build_time = [0] + list(map(int, input().split()))
        
    build_range = build_count + 1
    graph = [[] for _ in range(build_range)]
    indegree = [0 for _ in range(build_range)]
    dp = [0 for _ in range(build_range)]
    
    # 건설 순서 입력
    for _ in range(build_rule):
        origin, destination = map(int, input().split())
        graph[origin].append(destination)
        indegree[destination] += 1
    
    build_target = int(input())
    
    queue = deque()
    
    for idx in range(1, build_range):
        if indegree[idx] == 0:
            queue.append(idx)
            dp[idx] = build_time[idx]
        
    while queue:
        now = queue.popleft()
        for idx in graph[now]:
            indegree[idx] -= 1
            if indegree[idx] == 0:
                queue.append(idx)
            dp[idx] = max(dp[idx], dp[now] + build_time[idx])
        
    print(dp[build_target])

'''
1
4 4
10 1 100 10
1 2
1 3
2 4
3 4
4

1
4 0
10 10 10 9
4
'''