from collections import deque
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
q = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1: # 토마토가 있는 위치 큐에 삽입
            q.append((i, j))
dx = [1, -1, 0, 0]
dy = [0 , 0, -1, 1]

while q:
    x, y = q.popleft() # 현재 위치
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        # 그래프를 벗어나는 경우 pass
        if nx<0 or ny<0 or nx>=N or ny>=M:
            continue
        # 토마토가 없는 경우 pass
        if graph[nx][ny] == -1:
            continue

        if graph[nx][ny] == 0: # 익지 않은 토마토가] 있는경우
            graph[nx][ny] = graph[x][y] + 1 # 카운트 올리기 (날짜)
            q.append((nx, ny))
answer=0
flag = True
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0: # 안익는 상황일 경우
            flag = False
            break
        if graph[i][j] > answer:
            answer=graph[i][j]
if flag:
    print(answer-1)
else:
    print(-1)