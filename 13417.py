test_case = int(input())

for _ in range(test_case):
    card_length = int(input())
    card_info = list(map(str, input().split()))
    
    card_list = [card_info[0]]
    for idx in range(1, card_length):
        if ord(card_list[0]) >= ord(card_info[idx]):
            card_list.insert(0, card_info[idx])
        else:
            card_list.append(card_info[idx])
        
    
    for val in card_list:
        print(val, end="")
    print()