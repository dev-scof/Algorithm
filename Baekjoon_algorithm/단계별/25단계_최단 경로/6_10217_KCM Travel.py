# https://8iggy.tistory.com/156 참고
import heapq
import sys
input = sys.stdin.readline
# 소요 시간은 짧지만 비용이 비싼 경우,
# 소요 시간은 길지만 비용이 싼 경우
INF = int(1e9)
T = int(input())

for _ in range(T):
    n, m, k = map(int, input().split()) # 공항의 수 n, 총 지원비용 m, 티켓정보의 수 k
    graph={}
    for __ in range(k):
        u, v, c, t = map(int, input().split())
        graph[u] = graph.get(u, [])
        graph[u].append((v, c, t)) # u에서 v로가는데 필요한 비용c, 시간 d

    # [정점][비용] 2차원 배열 생성
    table = [[INF] * (m+1) for _ in range(n+1)]
    
    # 큐 선언 및 초기값 설정
    q = []
    heapq.heappush(q, (0, 0, 1)) # 1번 노드에서 시작
    
    while q:
        curTime, curCost, cur = heapq.heappop(q)
        
        # 현재 걸리는 시간이 테
        if curTime > table[cur][curCost] or cur not in graph:
            continue
        

        for node, c, t in graph[cur]:
            i_cost = c + curCost # i로 가는 비용
            i_time = t + curTime # i로 가는 시간
            if i_cost <= m and i_time < table[node][i_cost]:
                for i in range(i_cost, m+1):
                    if i_time < table[node][i]:
                        table[node][i] = i_time
                    else:
                        break
                heapq.heappush(q, (i_time, i_cost, node))
    if table[n][m] == INF:
        print('Poor KCM')
    else:
        print(table[n][m])