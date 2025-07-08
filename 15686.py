map_size, store_active = map(int, input().split())
map_info = [list(map(int, input().split())) for _ in range(map_size)]

store_list = []
house_list = []
blank_list = []
list_chk = [blank_list, house_list, store_list]

for r in range(map_size):
    for c in range(map_size):
        list_chk[map_info[r][c]].append([r,c])

def combine_dfs(no, path, result, n, k):
    if len(path) == k:
        result.append(path)
        return

    for i in range(no, n):
        combine_dfs(i + 1, path + [i], result, n, k)

result = []
combine_dfs(0, [], result, len(store_list), store_active)


min_distance = 1000000000

def get_distance(house_list, store_list):
    sum_distance = 0
    for house in house_list:
        min_distance = 1000000000
        for store in store_list:
            now_distance = abs(house[0] - store[0]) + abs(house[1] - store[1])
            if now_distance < min_distance:
                min_distance = now_distance
        sum_distance += min_distance
        
    return sum_distance

for case_store in result:
    new_store_list = []
    for idx in case_store:
        new_store_list.append(store_list[idx])
    
    now_sum_distance = get_distance(house_list, new_store_list)
    if now_sum_distance < min_distance:
        min_distance = now_sum_distance
        
print(min_distance)