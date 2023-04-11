import heapq
INF = 1e9
def dijkstra(start, table):
    q = []
    heapq.heappush(q, (0, start)) # start 넣기
    table[start] = 0 # 최단거리 테이블의 start 0
    while q:
        dist, now = heapq.heappop(q)
        if dist>table[now] or now not in graph:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost<table[i[0]]:
                table[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

for _ in range(int(input())):
    n, m, t = map(int, input().split())
    # 교차로, 도로, 목적지 후보의 개수
    s, g, h = map(int, input().split())
    # 출발, g, h
    graph = {}
    dist_candidate = [] # 목적지 후보

    # 그래프 생성
    for _ in range(m):
        a, b, d = map(int, input().split())
        # 양방향
        graph[a] = graph.get(a, [])
        graph[a].append((b, d))
        graph[b] = graph.get(b, [])
        graph[b].append((a, d))
    
    s_table = [INF]*(n+1) # 최단 거리 테이블
    dijkstra(s, s_table)
    s_to_g = s_table[g]
    s_to_h = s_table[h]

    cost = INF # 목적지로 가는 비용 INF로 초기화
    answer = 0 # 목적지는 0으로 초기화

    # 목적지 입력
    answer = []
    for _ in range(t):
        x = int(input())
        g_table = [INF]*(n+1)
        h_table = [INF]*(n+1)
    
        # s -> g -> h -> x
        if s_to_g < INF:
            dijkstra(h, h_table)
        # s-> h -> g -> x
        if s_to_h < INF:
            dijkstra(g, g_table)
        
        g_to_x = g_table[x]
        h_to_x = h_table[x]
        s_to_x = s_table[x]        

        course1 = s_to_g + g_table[h] + h_to_x # s->g->h->x
        course2 = s_to_h + h_table[g] + g_to_x # s->h->g->x

        # s에서 x로 가는 최단거리와, g-h 도로를 지났을 때의 비용이 같은 경우
        if course1 == s_to_x or course2 == s_to_x:
            answer.append(x)
    answer.sort()
    print(' '.join(map(str, answer)))