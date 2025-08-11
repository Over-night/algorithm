room_no = list(input())
num_list = [0 for _ in range(10)]
for no in room_no:
    num_list[int(no)] += 1
    
num_list[6] += num_list[9]
num_list[6] = num_list[6] // 2 + num_list[6] % 2

print(max(num_list[0:9]))