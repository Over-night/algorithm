for _ in range(int(input())):
    n, r = map(int, input().split())
    if r>n:
        n, r = r, n
    res = 1
    for i in range(n, n-r, -1):
        res *= i
    for i in range(r, 1, -1):
        res //= i
    print(res)