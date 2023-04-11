graph = {}
N = int(input())
M = int(input())
visited=set()
for _ in range(M):
    u, v = map(int, input().split())
    graph[u] = graph.get(u, [])+[v]
    graph[v] = graph.get(v, [])+[u]

def dfs(s):
    visited.add(s)
    for v in graph[s]:
        if v not in visited:
            dfs(v)
dfs(1)
print(len(visited)-1)