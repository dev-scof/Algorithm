import heapq
import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())
INF = 1e9
graph = dict()
reverse_graph = dict()
for _ in range(M):
    u, v, t = map(int, input().split())
    # u -> v로 가는 그래프
    graph[u] = graph.get(u, [])
    graph[u].append((v, t))

    # v -> u로 가는 그래프, 역방향 그래프 생성
    reverse_graph[v] = reverse_graph.get(v, [])
    reverse_graph[v].append((u, t))


def dijkstra(S, graph):
    '''
    다익스트라 알고리즘
    
    최단경로 테이블을 반환해준다.
    '''
    distance = [INF]*(N+1)
    q = []
    distance[S]=0
    heapq.heappush(q, (0, S))

    while q:
        dist, now = q.pop()

        if dist > distance[now] or now not in graph:
            continue

        for v, w in graph[now]:
            cost = dist + w
            if cost < distance[v]:
                distance[v]=cost
                heapq.heappush(q, (cost, v))
    return distance

answer = 0
N_to_X = dijkstra(X, reverse_graph) # 역방향 그래프를 사용함으로써 N -> X의 최단거리 테이블을 할당받는다.
X_to_N = dijkstra(X, graph) # 정상 그래프를 사용함으로써 X -> N의 최단거리 테이블을 할당받는다.


for i in range(1, N+1):
    if i==X:
        continue
    time = X_to_N[i] + N_to_X[i] # 시간을 계산한다
    if time > answer:
        answer = time
print(answer)