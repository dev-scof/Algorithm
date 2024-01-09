from collections import deque
m, n, h = map(int, input().split())
board=[]
dh=[1, -1, 0, 0, 0, 0]
di=[0, 0, 0, 0, 1, -1]
dj=[0, 0, 1, -1, 0, 0]
queue=deque()
for k in range(h):
    temp=[]
    for i in range(n):
        temp.append(list(map(int, input().split())))
    board.append(temp)
# idx
for k in range(h):
    for i in range(n):
        for j in range(m):
            if board[k][i][j]==1:
                queue.append((k, i, j))
day = 0
while queue:
    z, i, j = queue.popleft()
    for d in range(6):
        nz = dh[d]+z
        ni = di[d]+i
        nj = dj[d]+j
        if nz<0 or ni<0 or nj<0 or nz>=h or ni>=n or nj>=m:
            continue
        if board[nz][ni][nj]==0:
            queue.append((nz, ni, nj))
            board[nz][ni][nj] = board[z][i][j] + 1
answer=0
flag=True
for k in range(h):
    for i in range(n):
        for j in range(m):
            if board[k][i][j] == 0: # 안익는 상황일 경우
                flag = False
                break
            if board[k][i][j] > answer:
                answer=board[k][i][j]
if flag:
    print(answer-1)
else:
    print(-1)