import heapq
V, E = map(int, input().split())
S = int(input())
INF = 1e9 # 무한 설정
distance = [INF]*(V+1) # 최단 거리 테이블
graph = {} # 딕셔너리로 구현

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u]= graph.get(u, [])
    graph[u].append((v, w))

# 다익스트라
def dijkstra(start):
    q = [] # 힙에 저장되는 값 = (가중치, 노드번호)
    heapq.heappush(q, (0, start)) # 시작, 
    distance[start] = 0 # 시작과 시작의 거리는 0
    while q:
        dist, now = heapq.heappop(q) # 거리가 짧은 노드순으로 정렬됨
        
        if distance[now] < dist or now not in graph.keys():
            # 최단 경로 테이블에 저장되어있는 비용보다 비용이 크거나
            # 마지막 노드일 경우 pass
            continue

        for i in graph[now]: # 현재 노드에 연결되어있는 노드에 대해 반복
            cost = dist + i[1] # i[1]은 i[0]노드로 이동하는 비용을 의미
            if cost < distance[i[0]]: # i[0]는 노드번호, distance[i[0]]는 i[0] 노드에 가는 비용
                # 만약 i[0]로 이동하는 비용이 최단 거리 테이블에 저장되어있는 비용보다 적으면 -> 갱신 및 힙에 추가
                distance[i[0]] = cost # 최단 거리 테이블 갱신
                heapq.heappush(q, (cost, i[0])) # 힙에 (cost, i[0]) 삽입
dijkstra(S)
for i in range(1, V+1): # 모든 노드에 대해 반복
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
