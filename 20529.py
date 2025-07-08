from itertools import combinations

def get_distance(me, opponent):
    distance = 0
    for idx in range(4):
        distance += (0 if me[idx]==opponent[idx] else 1)
    return distance

def get_combinations(n, r):
    elements = list(range(0, n))
    comb_list = list(combinations(elements, r))
    return comb_list


MBTI_INFO = ['ENFJ', 'ENFP', 'ENTJ', 'ENTP', 'ESFJ', 'ESFP', 'ESTJ', 'ESTP', 'INFJ', 'INFP', 'INTJ', 'INTP', 'ISFJ', 'ISFP', 'ISTJ', 'ISTP']

MBTI_DISTANCE_MAP = {}
for mbti_me in MBTI_INFO:
    distance_map = {}
    for mbit_opponent in MBTI_INFO:
        distance_map[mbit_opponent] = get_distance(mbti_me, mbit_opponent)
        
    MBTI_DISTANCE_MAP[mbti_me] = distance_map

testcase = int(input())

for _ in range(testcase):
    mbti_chk = {
        mbti:0 for mbti in MBTI_INFO
    }
    personality_count = int(input())
    personality_info = list(map(str, input().split()))
    personality_search = []
    for mbti in personality_info:
        mbti_chk[mbti] += 1
        
    min_distance = 9
    for key, value in mbti_chk.items():
        if value >= 3:
            min_distance = 0
    if min_distance == 0:
        print(min_distance)
        continue
    
    for key, value in mbti_chk.items():
        if value >= 2:
            personality_search.append(key)
        if value >= 1:
            personality_search.append(key)
        
            
    if min_distance < 9:
        print(min_distance)
        continue

    testcase_distance = 0
    
    comb_list = get_combinations(personality_count, 3)

    min_distance = 10000000
    for comb in comb_list:
        distance = MBTI_DISTANCE_MAP[personality_search[comb[0]]][personality_search[comb[1]]] \
            + MBTI_DISTANCE_MAP[personality_search[comb[0]]][personality_search[comb[2]]] \
            + MBTI_DISTANCE_MAP[personality_search[comb[1]]][personality_search[comb[2]]]
        if min_distance > distance:
            min_distance = distance        
        
    print(min_distance)