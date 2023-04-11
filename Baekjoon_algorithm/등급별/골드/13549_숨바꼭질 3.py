import heapq
N, K = map(int, input().split())
INF = 1e9
max_N = 100_000
times = [INF]*(max_N+1)

def dijkstra(S):
    times[S] = 0
    q = []
    heapq.heappush(q, (0, S))
    while q:
        time, now = heapq.heappop(q)

        # X+1로 이동할 때
        if now+1 <= max_N and time+1 < times[now+1]:
            times[now+1] = time+1
            heapq.heappush(q, (time+1, now+1))
        # X-1로 이동할 때
        if now-1 >=0 and time+1 < times[now-1]:
            times[now-1]=time+1
            heapq.heappush(q, (time+1, now-1))
        # X*2로 이동할 때
        if 0 <= now*2 <= max_N and time < times[now*2]:
            times[now*2]=time
            heapq.heappush(q, (time, now*2))
dijkstra(N)
print(times[K])