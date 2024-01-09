N = int(input())
M = int(input())
graph = {}
visited = set()
def dfs(v):
    visited.add(v) # 방문
    if v not in graph: # key error을 반영한 코드, 시작점이 그래프에 없을 경우 -> 끝냄 
        return
    for i in graph[v]:
        if i not in visited:
            dfs(i)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a] = graph.get(a, []) + [b]
    graph[b] = graph.get(b, []) + [a]
dfs(1)
print(len(visited)-1) # 1은 제외