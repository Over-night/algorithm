import sys
sys.setrecursionlimit(100000000)

class Node:
    cost = 0
    
    def __init__(self, serial, sales):
        self._serial = serial
        self._sales = sales
        self._node = []
        self._parent = None
        self._chk = False
    def setParent(self, node):
        self._parent = node
    def addNode(self, node):
        self._node.append(node)
        self._node[-1].setParent(self)
    def getSalesList(self):
        return [self._sales] + [node._sales for node in self._node]
    
    def __str__(self):
        tmp = ''
        for node in self._node:
            tmp += f'{node._serial} '
        if self._parent != None:
            tmp += f'/ {self._parent._serial}'
        return f'{self._serial} | {self._sales} | ' + tmp

def search(head):
    if len(head._node) == 0:
        return
    
    # 현재 노드에서 최솟값 구하기 
    cost_min = head._sales
    cost_idx = -1
    for idx in range(len(head._node)):
        search(head._node[idx])
        if head._node[idx]._sales < cost_min:
            cost_min = head._node[idx]._sales
            cost_idx = idx
    
    # 이미 참석한 팀원이 있으면 pass
    if head._chk:
        return
    
    # 현재 노드 기준으로 최소 cost가 head인지 확인
    if cost_idx < 0:
        Node.cost += head._sales
        head._chk = True
        if head._parent != None:
            head._parent._chk = True
        #print(f'Head : {head._serial} | Min : {head._sales}\nCase: 현재 노드의 cost가 최소인 경우\n')
        return
    
    # 부모가 없거나 이미 체크한 경우
    if head._parent is None or head._parent._chk:
        Node.cost += cost_min
        head._chk = True
        if len(head._node[cost_idx]._node) > 0:
            head._node[cost_idx]._chk = True
        #print(f'Head : {head._serial} | Min : {cost_min}\nCase: 현재 노드의 자식노드 최솟값, 부모 없거나 체크완료\n')
        return
    
    # 부모 노드 기준으로 최소 cost가 현재 노드 head인지 확인
    parent = head._parent
    cost_parent_min = parent._sales
    cost_parent_idx = -1
    for idx in range(len(parent._node)):
        if parent._node[idx]._sales < cost_parent_min:
            cost_parent_min = parent._node[idx]._sales
            cost_parent_idx = idx
    
    # 부모 노드의 cost 최소 노드가 head 노드인 경우
    if cost_parent_idx >= 0 and head == parent._node[cost_parent_idx]:
        Node.cost += head._sales
        head._chk = True
        head._parent._chk = True
        #print(f'Head : {head._serial} | Min : {head._sales}\nCase: 부모의 자식노드 최솟값이 head의 것인 경우\n')
        return
    
    # 그 무엇도 아닌경우 : 부모의 자식노드 최소 + head의 자식노드 최소 vs head 노드 값 비교
    cost_total = cost_min + cost_parent_min
    if head._sales < cost_total:
        Node.cost += head._sales
        #print(f'Head : {head._serial} | Min : {head._sales}\nCase: 그 무엇도 아닌 경우 - head값이 더 작은 경우\n')
    else:
        Node.cost += cost_total
        if cost_parent_idx < 0:
            if parent._parent != None:
                parent._parent._chk = True
        else:
            if len(parent._node[cost_parent_idx]._node) > 0:
                parent._node[cost_parent_idx]._chk = True
        
        #print(f'Head : {head._serial} | Min : {cost_total}\nCase: 그 무엇도 아닌 경우 - head와 부모의 자식노드 최소값 합이 더 작은 경우\n')
    head._chk = True
    head._parent._chk = True
    

def solution(sales, links):
    length = len(sales) + 1
    # 노드 설정
    employees = [Node(0,0)]
    cnt = 1
    for sale in sales:
        employees.append(Node(cnt, sale))
        cnt += 1
    for link in links:
        employees[link[0]].addNode(employees[link[1]])
    
    # 탐색
    search(employees[1])

    #print(Node.cost)
    
    answer = Node.cost
    return answer