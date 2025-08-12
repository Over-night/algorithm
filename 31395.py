def getPairAmount(part_pair):    
    return (part_pair * (part_pair + 1)) // 2

sequence_size = int(input())
sequence = list(map(int, input().split()))

before_element = 0
part_pair = 0
pair_total = 0

for element in sequence:
    if before_element <= element:
        before_element = element
        part_pair += 1
    else:
        pair_total += getPairAmount(part_pair)
        part_pair = 1
        before_element = element
        
pair_total += getPairAmount(part_pair)

print(pair_total)
