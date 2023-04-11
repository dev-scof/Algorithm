'''
이코테 참조
'''
from collections import deque
N, M = map(int, input().split())
graph =[list(map(int, input())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft() # 현재 위치
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 그래프를 벗어나는 경우 pass
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            # 못지나가는 경우 pass
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 # 카운트 올리기
                q.append((nx, ny))
    return graph[N-1][M-1]

print(bfs(0,0))