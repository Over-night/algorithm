def search(idx, bishops, info, l_diagonal, r_diagonal, max_bishop):
    if idx >= len(info):
        if max_bishop[0] < bishops:
            max_bishop[0] = bishops
        return

    y, x = info[idx]
    l = y - x + s - 1
    r = y + x
    
    if not (l_diagonal[l] or r_diagonal[r]):
        l_diagonal[l] = r_diagonal[r] = True
        search(idx+1, bishops+1, info, l_diagonal, r_diagonal, max_bishop)
        l_diagonal[l] = r_diagonal[r] = False
        
    search(idx+1, bishops, info, l_diagonal, r_diagonal, max_bishop)


siro_max = [0]
kuro_max = [0]
    
s = int(input())
b = [list(map(int, input().split())) for _ in range(s)]

siro = []
kuro = []
for y_idx in range(s):
    for x_idx in range(s):
        if b[y_idx][x_idx] == 0:
            continue
        (siro if (y_idx + x_idx) % 2 == 0 else kuro).append((y_idx, x_idx))

# 대각선 범주화 
l_diagonal = [False for _ in range(s * 2)]
r_diagonal = [False for _ in range(s * 2)]
search(0, 0, siro, l_diagonal, r_diagonal, siro_max)

l_diagonal = [False for _ in range(s * 2)]
r_diagonal = [False for _ in range(s * 2)]
search(0, 0, kuro, l_diagonal, r_diagonal, kuro_max)

print(siro_max[0] + kuro_max[0])
