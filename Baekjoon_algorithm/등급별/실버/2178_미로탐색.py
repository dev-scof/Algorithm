from collections import deque
n, m = map(int, input().split())
board=[]
for i in range(n):
    board.append(list(map(int, input())))
i=j=0
q = deque()
q.append((i, j))
n_i=[0,0,1,-1]
n_j=[1,-1,0,0]

def show():
    for i in range(n):
        for j in range(m):
            print(board[i][j], end=' ')
        print()    
    print()
while q:
    i, j = q.popleft()
    for d in range(4):
        d_i=n_i[d]+i
        d_j=n_j[d]+j
        if d_i<0 or d_j<0 or d_i>=n or d_j>=m:
            continue
        if board[d_i][d_j]==1:
            board[d_i][d_j]=board[i][j]+1
            q.append((d_i, d_j))     
print(board[n-1][m-1])