from collections import deque
def show():
    for i in range(n):
        for j in range(m):
            print(board[i][j], end=' ')
        print()
    print()
m, n = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
queue = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 1: # 토마토가 있는 위치 큐에 삽입
            queue.append((i, j))
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
day=0
while queue:
    for q in range(len(queue)):
        x = queue.popleft()
        for di, dj in d:
            ni = x[0]+di
            nj = x[1]+dj
            if ni<0 or nj<0 or ni>=n or nj>=m:
                continue
            if board[ni][nj]==0:
                queue.append((ni, nj))
                board[ni][nj]=1
    day+=1
check=True
for line in board:
    if 0 in line:
        check=False
        break
if check:
    print(day-1)
else:
    print(-1)