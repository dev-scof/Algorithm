from collections import defaultdict
import sys
input = sys.stdin.readline
graph = defaultdict(list)
visited = set()
input()
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(now):
    if now in visited:
        return
    visited.add(now)
    for v in graph[now]:
        dfs(v)

dfs(1)
print(len(visited)-1)