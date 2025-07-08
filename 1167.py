class Line:
    def __init__(self, dest, cost):
        self.dest = dest
        self.cost = cost

class Vertex:
    def __init__(self, key):
        self.loc = key
        self.way = []
    def setLine(self, ipt):
        idx = 1
        while ipt[idx] != -1:
            self.way.append(Line(ipt[idx], ipt[idx+1]))
            idx += 2


vertex_amount = int(input())
LEN = vertex_amount + 1
vertex_map = [Vertex(i) for i in range(LEN)]

for _ in range(vertex_amount):
    ipt = list(map(int, input().split()))
    vertex_map[ipt[0]].setLine(ipt)

max_length = -1

for base in range(1, LEN):
    distance_map = [0 for _ in range[LEN]]

