import sys
input = sys.stdin.readline
n_i = [0, 0, 1, -1]
n_j = [1, -1, 0, 0]
def dfs(i, j):
    if i<0 or j<0 or i>=N or j>=M:
        return
    if Map[i][j] == 1:
        Map[i][j]=0
        for d in range(4):
            d_i = n_i[d] + i
            d_j = n_j[d] + j
            dfs(d_i, d_j)
    
for _ in range(int(input())):
    M, N, K = map(int, input().split())
    Map = [[0]*M for __ in range(N)]
    for b in range(K):
        j, i = map(int, input().split())
        Map[i][j] = 1
    cnt=0
    
    for i in range(N):
        for j in range(M):
            if Map[i][j] == 1:
                dfs(i, j)
                cnt+=1
    print(cnt)