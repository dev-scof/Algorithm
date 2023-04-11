from collections import deque
M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)]for j in range(H)]
q = deque()
for k in range(H):
    for i in range(N):
        for j in range(M):
            if graph[k][i][j] == 1:
                q.append((k, i, j))
# z, x, y 순
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
# 오, 왼, 앞, 뒤, 위, 아래
while q:
    z, x, y = q.popleft()
    for i in range(6):
        nx = x+dx[i]
        ny = y+dy[i]
        nz = z+dz[i]

        # 그래프를 벗어나는 경우 pass
        if nx<0 or nx>=N or ny<0 or ny>=M or nz<0 or nz>=H:
            continue
        # 토마토가 없는 경우 pass
        if graph[nz][nx][ny] == -1:
            continue
        if graph[nz][nx][ny] == 0:
            graph[nz][nx][ny] = graph[z][x][y] + 1
            q.append((nz,nx,ny))
answer=0
flag = True
for k in range(H):
    for i in range(N):
        for j in range(M):
            if graph[k][i][j] == 0: # 안익는 상황일 경우
                flag = False
                break
            if graph[k][i][j] > answer:
                answer=graph[k][i][j]
if flag:
    print(answer-1)
else:
    print(-1)