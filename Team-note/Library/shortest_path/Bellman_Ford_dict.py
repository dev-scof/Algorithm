import sys
input = sys.stdin.readline
INF = 1e9

# 정점의 개수, 간선의 개수 입력
N, M = map(int, input().split())

# 그래프 생성
graph = {}

# 최단 거리 테이블 생성
dist = [INF]*(N+1)

# 모든 간선 정보 입력
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a] = graph.get(a, [])
    graph[a].append((b, c))

def bellman_ford(s):
    # 시작 노드에 대해 최단 거리 테이블 초기화
    dist[s] = 0

    # 전체 n번 라운드 반복
    for _ in range(N):
        # 그래프에 있는 모든 정점에 대해 반복
        for v, e in graph.items():
            # v는 현재 노드, e는 연결된 간선
            for u, w in e: # v에 연결된 모든 정점에 대해 반복
                if dist[v] != INF and dist[u] > dist[v] + w:
                    dist[u] = dist[v] + w
                    
                    # 만약 마지막에도 갱신이 이루어진다면 
                    # 음의 간선이 있다는 것을 의미한다.
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