from collections import deque
import sys
input = sys.stdin.readline
def bfs(node):
    # visited 초기화
    visited = [-1] * (N+1)
    visited[node] = 0 # 현재 노드에 대해 갱신, 가중치 0
    q = deque()
    q.append(node)
    while q:
        now = q.popleft() # 큐에서 가져오기
        for n, cost in graph[now]:
            # 연결된 간선에 대해 다음을 반복한다.
            if visited[n] == -1:
                # 방문하지 않았다면 -> 갱신 및 큐에 추가
                visited[n] = visited[now] + cost
                q.append(n)
    return visited

# 그래프 입력
N = int(input())
graph = dict()
for _ in range(N):
    line = list(map(int, input().split()))
    v = line[0]
    for i in range(1, len(line)//2):
        graph[v] = graph.get(v, [])
        graph[v].append([line[i*2-1], line[i*2]])

# 1. bfs 수행
res = bfs(4)
# 2. 최대 가중치를 가진 값(외부노드-잎) 가져오기
idx = res.index(max(res))
# 3. 외부노드-잎에서부터 bfs수행
print(max(bfs(idx)))