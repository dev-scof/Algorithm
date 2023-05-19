import heapq
import sys
input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
INF = 1e9
graph = dict()
distance = [INF]*(V+1)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u] = graph.get(u, [])
    graph[u].append((v, w))

def dijkstra(S):
    distance[S]=0 # 최단경로 초기화
    q = []
    heapq.heappush(q, (0, S)) # 현재 비용과, 정점 추가
    while q:
        dist, now = heapq.heappop(q) # dist : S부터 v까지 가는 거리

        if distance[now] < dist or now not in graph:
            # 현재 방문한 노드까지 가는 거리(dist)가 최단 경로보다 큰 경우
            # // 이미 최단거리일 경우 -> 갱신할 필요없음
            # 마지막 노드일 경우(이동할 정점이 없을 경우) -> 패스
            continue

        for v, w in graph[now]:
            cost = dist+w # 현재에서 w가중치만큼 더한것이 비용임
            if cost < distance[v]: # 만약 이 거리가 최단 경로보다 작은 경우 => 갱신해줄필요가 있다.
                distance[v] = cost
                heapq.heappush(q, (cost, v))

dijkstra(K)
for i in range(1, V+1): # 모든 노드에 대해 반복
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])


def dijkstra(s):
    distance[s]=0
    q = []
    heapq.heappush(q, (0, s))
    while q:
        dist, now = heapq.heappop(q)

        if now not in graph or dist > distance[now]:
            continue
        
        # 인접한 노드에 대해 반복
        for v, w in graph[now]:
            cost = dist+w
            if cost < distance[v]:
                # 갱신
                distance[v]=cost
                heapq.heappush(q, (cost, v))