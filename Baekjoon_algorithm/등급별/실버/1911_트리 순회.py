class Node:
    def __init__(self, value, left, right) -> None:
        self.value=value
        self.left=left
        self.right=right
N = int(input())
tree = dict()
for _ in range(N):
    value, left, right = input().split()
    tree[value] = Node(value, left, right)

result1=[]
result2=[]
result3=[]

def preOrder(node):
    # 전위순회 : 먼저 방문한다.
    result1.append(node)
    if tree[node].left != '.':
        preOrder(tree[node].left)
    if tree[node].right != '.':
        preOrder(tree[node].right)
def inOrder(node):
    # 중위순회 : 중간에 방문한다.
    if tree[node].left != '.':
        inOrder(tree[node].left)
    result2.append(node)
    if tree[node].right != '.':
        inOrder(tree[node].right)

def postOrder(node):
    # 후위 순회 : 나중에 방문한다.
    if tree[node].left != '.':
        postOrder(tree[node].left)
    if tree[node].right != '.':
        postOrder(tree[node].right)
    result3.append(node)

preOrder('A')
inOrder('A')
postOrder('A')

print(''.join(result1))
print(''.join(result2))
print(''.join(result3))