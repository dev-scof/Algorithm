from collections import deque
N, M, V = map(int, input().split())
graph = {}
for _ in range(M):
    u, v = map(int, input().split())
    # 
    graph[u] = graph.get(u, [])+[v]
    graph[v] = graph.get(v, [])+[u]

dfs_visited=set()
for v in graph:
    graph[v].sort()
    
def dfs(s):
    print(s, end=' ')
    dfs_visited.add(s)

    if s not in graph:
        return
    for v in graph[s]:
        if v not in dfs_visited:
            dfs(v)

def dfs_stack(s):
    stack = [s]
    dfs_visited_stack = set()
    while stack:
        n = stack.pop()
        if n not in graph:
            continue
        if n not in dfs_visited_stack:
            # 방문처리
            print(n, end=' ')
            dfs_visited_stack.add(n)
            stack.extend(list(sorted(graph[n], reverse=True)))
        
def bfs(s):
    queue = deque()
    queue.append(s)
    bfs_visited=set()
    while queue:
        cur = queue.popleft()
        print(cur, end=' ')
        if cur not in graph:
            continue
        if cur not in bfs_visited:
            bfs_visited|=set(graph[cur])
            queue.extend(graph[cur])
        
dfs(V)
print()
dfs_stack(V)
print()
# bfs(V)