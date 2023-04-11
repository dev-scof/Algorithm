import sys
import heapq
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = dict()
INF = 1e9
distance = [INF]*(N+1)
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u] = graph.get(u, [])
    graph[u].append((v, w))

def dijkstra(S):
    distance[S] = 0
    q = []
    heapq.heappush(q, (0, S))
    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now] or now not in graph:
            continue

        for v, w in graph[now]:
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))

start, end = map(int, input().split())
dijkstra(start)
print(distance[end])