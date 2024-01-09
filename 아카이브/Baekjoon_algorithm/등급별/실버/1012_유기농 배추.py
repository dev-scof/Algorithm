def dfs(i, j):
    if i<=-1 or i>=n or j<=-1 or j>=m:
        return False
    if board[i][j]==1:
        board[i][j]=0
        dfs(i, j+1)
        dfs(i, j-1)
        dfs(i+1, j)
        dfs(i-1, j)
        return True
    return False
t=int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    cnt=0
    board=[[0]*m for __ in range(n)]
    for __ in range(k):
        j, i = map(int, input().split())
        board[i][j]=1
    for i in range(n):
        for j in range(m):
            if board[i][j]==1:
                dfs(i, j)
                cnt+=1
    print(cnt)