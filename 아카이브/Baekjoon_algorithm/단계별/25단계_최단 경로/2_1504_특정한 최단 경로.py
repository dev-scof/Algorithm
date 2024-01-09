import heapq
N, E = map(int, input().split())
INF = 1e9
start_v1 = [INF]*(N+1)
start_v2 = [INF]*(N+1)
start_1 = [INF]*(N+1)
graph={}
for _ in range(E):
    a, b, c = map(int, input().split())
    # 양방향
    graph[a] = graph.get(a, [])
    graph[a].append((b, c))
    graph[b] = graph.get(b, [])
    graph[b].append((a, c))
V1, V2 = map(int, input().split())
def dijkstar(s, distance):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist>distance[now] or now not in graph:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstar(V1, start_v1) # v1 시작
#print('v1 = ',V1, 'v1_to_v2_dist = ', start_v1, 'v1에서 v2로 가는 비용',start_v1[V2])
dijkstar(V2, start_v2) # v2 시작
#print('v2 = ',V2, 'start_v2 = ', start_v2, 'v2에서 v1로 가는 비용',start_v2[V1])
dijkstar(1, start_1) # 1 시작
#print('1->v1 = ', start_1[V1], '1->v2 = ', start_1[V2])
cost1 = start_1[V1]+start_v1[V2]+start_v2[N] # 1->v1->v2->N
cost2 = start_1[V2]+start_v2[V1]+start_v1[N] # 1->v2->v1->N
if cost1 < cost2:
    if cost1>=INF:
        print('-1')
    else:
        print(cost1)
else:
    if cost2>=INF:
        print('-1')
    else:
        print(cost2)