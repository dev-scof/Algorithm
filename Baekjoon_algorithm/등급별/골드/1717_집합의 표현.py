import sys

sys.setrecursionlimit(100000)

# 루트 노드를 찾는 함수
def find_root(x):
    if parent[x] == x:
        return x
    parent[x] = find_root(parent[x])
    return parent[x]

# 두 노드를 같은 집합으로 합치는 함수
def union(x, y):
    root_x = find_root(x)
    root_y = find_root(y)

    # 루트 노드가 다르면 합치기
    if root_x != root_y:
        parent[root_y] = root_x

n, m = map(int, input().split())

# 각 노드의 부모를 저장하는 리스트
parent = [i for i in range(n+1)]
print(parent)
for i in range(m):
    op, a, b = map(int, input().split())
    
    # 합집합 연산
    if op == 0:
        union(a, b)
        print(parent)
    # 같은 집합에 포함되어 있는지 확인하는 연산
    else:
        root_a = find_root(a)
        root_b = find_root(b)

        if root_a == root_b:
            print("YES")
        else:
            print("NO")