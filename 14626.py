isbn = input()

val_sum = 0
idx = -1

for i in range(len(isbn)):
    if isbn[i] == '*':
        idx = i
    else:
        val_sum += int(isbn[i]) * (1 if i%2==0 else 3)


div10 = 10 - val_sum % 10
div10 = div10 if div10 < 10 else 0
chk = 0

while chk*(1 if idx%2==0 else 3) % 10 != div10:
    chk += 1

print(chk)