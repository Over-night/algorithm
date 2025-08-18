a, b = map(int, input().split())

print(a+b+((a if a < b else b) // 10))