N = int(input())
graph = []
visited = set()
answer = []
for _ in range(N):
    graph.append(list(map(int, input())))

di = [0,0,1,-1]
dj = [1,-1,0,0]
def dfs(pos, visited):
    visited.add(pos) # 방문처리
    i, j = pos[0], pos[1]
    graph[i][j]=0 # 방문처리
    for k in range(4):
        ni = i+di[k]
        nj = j+dj[k]
        if ni<0 or ni>=N or nj<0 or nj>=N:
            continue
        if graph[ni][nj] == 1:
            if (ni, nj) not in visited:
                dfs((ni, nj), visited)
                
cnt=0
for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            visited = set()
            dfs((i, j),visited)
            answer.append(len(visited))
            cnt+=1
answer.sort()
print(cnt)
for ans in answer:
    print(ans)
for i in range(N):
    for j in range(N):
        print(graph[i][j], end=' ')
    print()