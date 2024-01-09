# 음의 가중치를 사용하기에 벨만 포드 or SPFA 알고리즘을 사용한다.
import heapq
INF = 1e9
N, M = map(int, input().split())
graph = {}
dist = [INF]*(N+1)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a] = graph.get(a, [])
    graph[a].append((b, c))

def bellman_ford(s):
    dist[s] = 0
    for _ in range(N):
        for v, e in graph.items():
            # v는 현재 노드, e는 연결된 간선리스트
            for u, w in e:
                # u는 연결된 노드, w는 가중치
                if dist[v] != INF and dist[u] > dist[v] + w:
                    dist[u] = dist[v] + w
                    if _ == N-1:
                        return True
    return False
    
if bellman_ford(1):
    print(-1)
else:
    for i in range(2, N + 1):
        # 도달할 수 없는 경우, -1 출력
        if dist[i] == INF:
            print("-1")
        # 도달할 수 있으면 거리 출력
        else:
            print(dist[i])