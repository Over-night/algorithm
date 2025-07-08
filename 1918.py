notation = input()

priority = {
    '*': 3, '/': 3,
    '+' : 2, '-' : 2,
    '(' : 1, ')' : 0
}

stack = []

for val in notation:
    if val not in priority:
        print(val, end='')
        continue
    
    if val == '(':
        stack.append(val)
        continue
    
    if val == ')':
        key = stack.pop()
        while key != '(':
            print(key, end='')
            key = stack.pop()
        continue

    p = priority[val]
    while len(stack) > 0 and priority[stack[-1]] >= p:
        key = stack.pop()
        print("" if key == '(' else key, end="")
    stack.append(val)


while len(stack) > 0:
    key = stack.pop()
    print("" if key == '(' else key, end="")
