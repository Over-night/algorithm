number_count = int(input())
number_list = list(map(int, input().split(' ')))
operator_list = list(map(int, input().split(' ')))

max_val = -1000000001
min_val = 1000000001

def calculator(a, b, oper):
    if oper == 0:
        return a+b
    if oper == 1:
        return a-b
    if oper == 2:
        return a*b
    if oper == 3:
        return a//b if a > 0 else -a//b * -1
    
def simulation(val, idx):
    global number_count, number_list, operator_list, max_val, min_val
    
    # 계산 종료 : 최대 최소값 확인
    if idx >= number_count:
        if val > max_val:
            max_val = val
        if val < min_val:
            min_val = val
        return
    
    for i in range(4):
        if operator_list[i] == 0:
            continue
    
        operator_list[i] -= 1
        simulation(calculator(val, number_list[idx], i), idx+1)
        operator_list[i] += 1    
            
simulation(number_list[0], 1)
         
print(max_val)
print(min_val)

