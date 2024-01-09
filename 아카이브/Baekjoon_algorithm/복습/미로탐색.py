from collections import deque
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

def bfs(pos):
    q = deque()
    q.append(pos)
    num=1
    di = [0,0,1,-1]
    dj = [1,-1,0,0]
    while q:
        i, j = q.popleft()
        # 현재 위치에 대해, 주변의 1을 갱신
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]
            if ni<0 or ni>=N or nj<0 or nj>=M:
                continue
            if graph[ni][nj]==1:
                graph[ni][nj]=graph[i][j]+1
                q.append((ni, nj))
        num+=1

    return num
bfs((0,0))
print(graph[N-1][M-1])


for i in range(N):
    for j in range(M):
        print(graph[i][j], end=' ')
    print()