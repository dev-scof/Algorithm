'''
find / union을 이용하는 문제
'''
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x

component = set()

for _ in range(m):
    u, v = map(int, input().split())
    
    if find(u) != find(v):
        union(u, v)

for i in range(1, n+1):
    component.add(find(i))

print(len(component))


'''
처음의 접근
dfs를 수행한 개수로 접근했다.


import sys
sys.setrecursionlimit(10000)
N, M = map(int, input().split())
graph = {}
for _ in range(M):
    u, v = map(int, input().split())
    graph[u] = graph.get(u, []) + [v]
    graph[v] = graph.get(v, []) + [u]


def dfs(s):
    visited.append(s)
    for v in graph[s]:
        if v not in visited:
            dfs(v)

visited = []
answer = 0
for v in graph:
    if v not in visited:
        answer+=1
        dfs(v)
print(answer)
'''