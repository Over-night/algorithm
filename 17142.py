class Locate:
    def __init__(self, row, col):
        self._row = row
        self._col = col
        
def combine(n, k):
    result = []
    combine_dfs(0, [], result, n, k)
    return result

def combine_dfs(no, path, result, n, k):
    if len(path) == k:
        result.append(path)
        return

    for i in range(no, n):
        combine_dfs(i + 1, path + [i], result, n, k)

BLANK = 0
WALL = 1
VIRUS = 2
VIRUS_ACTIVE = 3

map_size, virus_active_count = map(int, input().split())
map_info = [list(map(int, input().split())) for _ in range(map_size)]

virus_list = []
blank_count = 0
for r in range(map_size):
    for c in range(map_size):
        if map_info[r][c] is BLANK:
            blank_count += 1
        elif map_info[r][c] is VIRUS:
            virus_list.append(Locate(r,c))            

dir_list = [
    Locate(-1,0),
    Locate(1,0),
    Locate(0,-1),
    Locate(0,1)
]

if blank_count == 0:
    print(0)
    exit()

def simulation():
    global map_size, map_info, virus_active_count, virus_list, blank_count
    
    min_spread = 1000000000
    case_active = combine(len(virus_list), virus_active_count)
    
    for instance in case_active:
        instance_map = [[map_info[r][c] for c in range(map_size)] for r in range(map_size)]
        
        # 바이러스 활성화
        instance_blank_count = blank_count
        instance_virus = []
        step = []
        for idx in instance:
            instance_virus.append(virus_list[idx])
            instance_map[virus_list[idx]._row][virus_list[idx]._col] = VIRUS_ACTIVE
            step.append(0)
        
        st = virus_active_count
        ed = -1
        
        while st > ed + 1:
            ed += 1
            
            # 최소 전파수보다 넘을경우 continue
            if step[ed] >= min_spread:
                break
            
            for dir in dir_list:
                tmp_row = instance_virus[ed]._row + dir._row
                tmp_col = instance_virus[ed]._col + dir._col
                
                if tmp_row < 0 or tmp_col < 0 or tmp_row >= map_size or tmp_col >= map_size:
                    continue
                # 벽이거나 활성 바이러스일 경우
                if instance_map[tmp_row][tmp_col] % 2 != 0:
                    continue
                
                #바이러스 활성화
                instance_blank_count -= 1 if instance_map[tmp_row][tmp_col] is BLANK else 0
                instance_map[tmp_row][tmp_col] = VIRUS_ACTIVE
                instance_virus.append(Locate(tmp_row,tmp_col))
                step.append(step[ed] + 1)
                st += 1
            
            
            # 모든 칸이 다 찰 경우
            if instance_blank_count == 0:
                min_spread = step[-1]
                break
            
            print(step[ed], ed)
            for r in instance_map:
                for c in r:
                    print(c, end=" ")
                print()
        
        print('-------------------------------------------')
    
    return min_spread 
        
result = simulation()
print(-1 if result == 1000000000 else result)
