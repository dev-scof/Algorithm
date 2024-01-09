class Node:
    def __init__(self, data, left, right):
        self.left = left
        self.data = data
        self.right = right
N = int(input())

# dict 트리
tree = dict()
for _ in range(N):
    data, left, right = input().split()
    tree[data] = Node(data, left, right)
# 결과 리스트
result1 = []
result2 = []
result3 = []

def preOrdertraversal(node):
    result1.append(node)
    if tree[node].left != '.':
        preOrdertraversal(tree[node].left)
    if tree[node].right != '.':
        preOrdertraversal(tree[node].right)
def inOrdertraversal(node):
    if tree[node].left != '.':
        inOrdertraversal(tree[node].left)
    result2.append(node)
    if tree[node].right != '.':
        inOrdertraversal(tree[node].right)
def postOrdertraversal(node):
    if tree[node].left != '.':
        postOrdertraversal(tree[node].left)
    if tree[node].right != '.':
        postOrdertraversal(tree[node].right)
    result3.append(node)


preOrdertraversal('A')
inOrdertraversal('A')
postOrdertraversal('A')

print(''.join(result1))
print(''.join(result2))
print(''.join(result3))
'''
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
'''
