expression_length = int(input())
expression_data = input()

def expression_str2list(expression):
    expression = list(expression)
    for idx in range(0,len(expression),2):
        expression[idx] = int(expression[idx])
    return expression

def calculate_operator(expression):
    expression_list = expression_str2list(expression)
    expression_calmul = []
    idx = 0
    while idx < len(expression_list):
        if expression_list[idx] != '*':
            expression_calmul.append(expression_list[idx])
        else:
            expression_calmul[-1] = expression_list[idx-1] * expression_list[idx+1]
            idx += 1   
        idx += 1

    result = expression_calmul[0]
    for idx in range(2,len(expression_calmul),2):
        result += expression_calmul[idx] * (1 if expression_calmul[idx-1] == '+' else -1)
    return result

num_count = expression_length // 2 + 1
dp = [[0] + [0 for _ in range(num_count)] for _ in range(num_count+1)]




print(calculate_operator(expression_data))


# for idx in range(len(dp)):
#     break

'''
0 8
0 2
'''