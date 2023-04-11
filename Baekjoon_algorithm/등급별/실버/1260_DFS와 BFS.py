from collections import deque
n, m, s = map(int, input().split())
graph = {}
# 그래프 입력
for i in range(m):
    a, b = map(int, input().split())
    graph[a] = graph.get(a, [])+[b]
    graph[b] = graph.get(b, [])+[a]

for v in graph:
    graph[v].sort()

dfs_visited=set()
def dfs(s):
    print(s, end=' ')
    dfs_visited.add(s)
    for v in graph[s]:
        if v not in dfs_visited:
            dfs(v)
dfs(s)
print()
def bfs(s):
    queue = deque()
    visited=set()
    queue.append(s)
    while queue:
        v = queue.popleft()
        if v not in visited:
            visited.add(v)
            print(v, end=' ')
            queue.extend(graph[v])
bfs(s)