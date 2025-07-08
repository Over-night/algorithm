class box:
    def self(self, row, col, val):
        self._row = row
        self._col = col
        self._val = val

box_count, difference_standard = map(int, input().split())
box_list = [list(map(int, input().split()))]
for i in range(0, box_count):
    box_list[i] = box(0, i, box_list[i])
    
def step_1():
    global box_list, box_count
    
    min_value = 100000000
    for i in range(box_count):
        if box_list[0][i] < min_value:
            min_value = box_list[0][i]
            
    for i in range(box_count):
        if box_list[0][i] == min_value:
            box_list[0][i] += 1

def step_2():
    global box_list, box_count
    
    weight = 1
    step = 0
    box_left = box_count
    
    while weight <= box_left:
        for i in ran
        
        
        box_left -= weight
        step += 1
        if step >= 2:
            step = 0
            weight += 1