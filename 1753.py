class Line:
    def __init__(self, no):
        self._no = no
        self._link = {}
    def setLink(self, dest, weight):
        if dest not in self._link or self._link[dest] > weight:
            self._link[dest] = weight

vertex, edge = map(int, input().split())
start = int(input())

range_to = vertex + 1
INF = 2000000
maps = [None] + [Line(i) for i in range(1, range_to)]
weights = [INF for _ in range(range_to)]
check = [False for _ in range(range_to)]

for _ in range(edge):
    orig, dest, weight = map(int, input().split())
    maps[orig].setLink(maps[dest], weight)


def search(weights, check, location, cost):
    if check[location._no]:
        return
    
    check[location._no] = True

    if cost < weights[location._no]:
        weights[location._no] = cost

    for link, weight in location._link.items():
        search(weights, check, link, cost+weight)
    
    check[location._no] = False

search(weights, check, maps[start], 0)

for i in range(1, range_to):
    print('INF' if weights[i] == INF else weights[i])