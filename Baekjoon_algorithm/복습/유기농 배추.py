
di = [0,0,1,-1]
dj = [1,-1,0,0]
def dfs(i, j):
    graph[i][j]=0 # 방문처리
    for k in range(4):
        ni = i+di[k]
        nj = j+dj[k]
        if ni<0 or ni>=N or nj<0 or nj>=M:
            continue
        if graph[ni][nj]==1:
            dfs(ni, nj)

T = int(input())
answer =[]
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]
    # 그래프 생성
    for __ in range(K):
        j, i = map(int, input().split())
        graph[i][j]=1
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j]==1:
                dfs(i, j)
                cnt+=1
    answer.append(cnt)


for ans in answer:
    print(ans)