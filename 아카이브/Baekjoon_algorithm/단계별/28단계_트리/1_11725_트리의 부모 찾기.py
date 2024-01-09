from collections import defaultdict, deque
N = int(input())
graph = defaultdict(list)
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
keys = deque(sorted(graph.keys()))
parent = [0]*(N+1)
def bfs(graph):
    queue = deque([1]) # 1부터시작
    visited = set()
    parent[1] = 1
    while queue:
        now = queue.popleft()
        for edge in graph[now]:
            if edge not in visited:
                parent[edge] = now
                queue.append(edge)
                visited.add(edge)
bfs(graph)
for i in range(2, N+1):
    print(parent[i])