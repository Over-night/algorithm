import sys
sys.setrecursionlimit(10000)

class Binary_Node():
    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None

node_info = []
try:
    while True:
        node_info.append(int(input()))
except:
    pass

binary_tree = Binary_Node(node_info[0])

def searchnode_back(node):
    if node._left != None:
        searchnode_back(node._left)
    if node._right != None:
        searchnode_back(node._right)
    print(node._value)
    
for idx in range(1, len(node_info)):    
    value = node_info[idx]
    point = binary_tree

    while True:
        if value < point._value:
            if point._left == None:
                point._left = Binary_Node(value)
                break
            else:
                point = point._left
        else:
            if point._right == None:
                point._right = Binary_Node(value)
                break
            else:
                point = point._right
                
searchnode_back(binary_tree)