import sys
sys.setrecursionlimit(100000)
N = int(input())

tree = dict()
for _ in range(N-1):
    node1, node2 = map(int, input().split())
    tree[node1] = tree.get(node1, []) + [node2]
    tree[node2] = tree.get(node2, []) + [node1]

visited=set()
result=[1]*(N+1)
def find_parent(node):
    if node not in visited:
        visited.add(node)
    for edge in tree[node]:
        if edge not in visited:
            result[edge]=node
            find_parent(edge)
    return node
    
find_parent(1)
for i in range(2, len(result)):
    print(result[i])

'''
각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
                1
            6       4
        3         2   7
    5
'''