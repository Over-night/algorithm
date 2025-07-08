class Deep:
    def __init__(self, key):
        self.key = key
        self.deep = 0

    def __lt__(self, other):
        return self.deep > other.deep
    
    def setDeep(self, deep):
        self.deep = deep.deep + 1

class Root:
    def __init__(self, dest, cost):
        self.dest = dest
        self.cost = cost

    def __lt__(self, other):
        return self.cost > other.cost
    
    def addCost(self, cost):
        self.cost += cost

class Node:
    def __init__(self, key):
        self.key = key
        self.root = []
        self.root_max = 0
        self.sum_max = 0
    
    
    def addRoot(self, dest, cost):
        self.root.append(Root(dest, cost))
    
    def findCurrentCost(self):
        self.root.sort()

        self.root_max = self.root[0].cost
        self.sum_max = self.root[0].cost + (self.root[1].cost if len(self.root) > 1 else 0)

        return self.sum_max

node_amount = int(input())
node_map = [None] + [Node(i) for i in range(node_amount)]
node_deep = [Deep(i) for i in range(node_amount+1)]
max_cost = 0

for _ in range(node_amount-1):
    orig, dest, cost = map(int, input().split())
    node_deep[dest].setDeep(node_deep[orig])
    node_map[orig].addRoot(dest, cost)

node_deep = sorted(node_deep[1:])

for deep in node_deep:
    key = deep.key
    if len(node_map[key].root) == 0:
        continue

    for idx in range(len(node_map[key].root)):
        node_map[key].root[idx].addCost(node_map[node_map[key].root[idx].dest].root_max)
        
    current_max = node_map[key].findCurrentCost()
    if current_max > max_cost:
        max_cost = current_max

print(max_cost)