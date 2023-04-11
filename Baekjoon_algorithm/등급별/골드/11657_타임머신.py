# 그래프 생성
import heapq
INF = 1e9
N, M = map(int, input().split())
graph = {}
dist = [INF]*(N+1)
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u] = graph.get(u, [])
    graph[u].append((v, w))

# 벨만포드 알고리즘
def bellman_ford(S):
    # 처음 정점의 최단경로는 0 지정
    dist[S] = 0
    # n번의 라운드 반복
    for n in range(N):
        # 모든 간선을 확인한다.
        for key, edges in graph.items():
            # 현재 key에 해당하는 edge에 대해 반복한다
            for edge in edges:
                # cost : key를 거쳐서 다른 노드(edge[0])으로 가는 비용
                cost = dist[key]+edge[1]
                if dist[key] != INF and dist[edge[0]] > cost:
                    dist[edge[0]] = cost
                    if n == N-1:
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