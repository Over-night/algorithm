import heapq

class DualPriorityQueue:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.delete_delay = set()
        
    def insert(self, val):
        heapq.heappush(self.min_heap, val)
        heapq.heappush(self.max_heap, -val)
        
    def delete_min(self):
        while self.min_heap and self.min_heap[0] in self.delete_delay:
            self.delete_delay.remove(self.min_heap[0])
            heapq.heappop(self.min_heap)
        if self.min_heap:
            val = heapq.heappop(self.min_heap)
            self.delete_delay.add(-val)

    def delete_max(self):
        while self.max_heap and -self.max_heap[0] in self.delete_delay:
            self.delete_delay.remove(-self.max_heap[0])
            heapq.heappop(self.max_heap)
        if self.max_heap:
            val = -heapq.heappop(self.max_heap)
            self.delete_delay.add(val)

    def get_result(self):
        while self.min_heap and self.min_heap[0] in self.delete_delay:
            self.delete_delay.remove(self.min_heap[0])
            heapq.heappop(self.min_heap)
        while self.max_heap and -self.max_heap[0] in self.delete_delay:
            self.delete_delay.remove(-self.max_heap[0])
            heapq.heappop(self.max_heap)
        if self.min_heap and self.max_heap:
            return -self.max_heap[0], self.min_heap[0]
        return None

testcase_amount = int(input())

for _ in range(testcase_amount):
    task_amount = int(input())
    queue = DualPriorityQueue()
    
    for _ in range(task_amount):
        task, num = input().split()
        num = int(num)
        
        if task == 'I':
            queue.insert(num)
        else:
            if num == 1:
                queue.delete_max()
            else:
                queue.delete_min()
    
    result = queue.get_result()
    
    if result == None:
        print('EMPTY')
    else:
        print(*result) 