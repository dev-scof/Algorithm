T = int(input())
def dfs(x, y):
    if x<=-1 or x>=N or y<=-1 or y>=M:
        return False
    if graph[x][y] == True:
        graph[x][y] = False # 방문처리
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[False]*M for _ in range(N)]
    result = 0 # 결과 값

    for k in range(K):
        y, x = map(int, input().split())
        graph[x][y] = True # 배추 위치 초기화
    
    for i in range(N):
        for j in range(M):
            if dfs(i,j)==True:
                result+=1
    print(result)


