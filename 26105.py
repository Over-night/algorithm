n = int(input())
stick_size = list(map(int, input().split()))

# 힌지 위치 구하기
hinge_loc = []
count = 0
for stick in stick_size:
    count += stick
    hinge_loc.append(stick)
hinge_loc.pop()
sticks_length = count

bottom_length = 0
fold_length = 0
index = 0
while index < n:
    bottom_length += stick_size[index]
    
    # 접을 수 없는 경우
    if fold_length > bottom_length:
         index += 1
         continue
     
    # 접을 수 있는 경우
    sticks_length -= bottom_length
    if bottom_length > fold_length:
        fold_length = bottom_length
    bottom_length = 0
    index += 1
    
print(fold_length if fold_length > sticks_length else sticks_length)


'''
1 3 2 3 4 2 2

1
3 2 3 4 2 2

3
2 3 4 2 2

3

5 4 2 2

5

4 2 2

5

6 2

6

2


3
2 3 4 2 2

3
2 3 4 2 2

3 3
2 4 2 2

'''