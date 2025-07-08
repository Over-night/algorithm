cnt = int(input())

stack = [[] for _ in range(4)]
stack[0].append(1)
stack[1].append(0)
for i in range(cnt, 0, -1):
    stack[1].append(i)

def dp(cnt, weight):
    global stack 
    if cnt <= 0: return
    dp(cnt-1, abs(weight-1))
    a = stack[1][-1].pop()
    stack[stack[0][weight]].append(a)
    if len(stack[1]) > 0:


if cnt > 20:
    print(2**cnt - 1)
else:
    print(dp(cnt, cnt%2))
