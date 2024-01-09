# https://ca.ramel.be/82
# BFS 알고리즘을 순환하면서, 
# 벽을 뚫을 수 있는 상태이고, 벽을 만난다면 벽을 뚫어주고 + 1을 해준다. 
# 아직 방문하지 않았고 벽이 아니라면 + 1을 해준다
from collections import deque
N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)] # 그래프 입력
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


def bfs():
    q = deque()
    q.append((0, 0, 1)) # 현 위치, (0,0)에서 벽을 안뚫은 상태 1
    visited = [[[0]*2 for _ in range(M)] for __ in range(N)] # 방문 여부
    visited[0][0][1] = 1 # visited[x][y][w] 
    # w는 벽을 뚫었는지 알리는 변수, 
    # 0:벽을 뚫었음, 1:벽을 안뚫었음
    while q:
        x, y, w = q.popleft() # 위치, 벽 뚫은지 여부
        # print('x = ', x, 'y = ', y, 'w = ', w)
        if x == N-1 and y == M-1: # 마지막 위치라면 함수 종료
            '''
            for z in range(2):
                for i in range(N):
                    for j in range(M):
                        print(visited[i][j][z], end=' ')
                    print()
            '''
            return visited[x][y][w]
        for i in range(4):
            nx = x + dx[i] # 이동할 x
            ny = y + dy[i] # 이동할 y
            if 0<=nx<N and 0<=ny<M: # 그래프 안에 있으면
                if graph[nx][ny] == 1 and w==1: # 이동할 곳이 벽인데, 한번도 안뚫은 상태(뚫을 수 있는 상태)라면
                    visited[nx][ny][0] = visited[x][y][1] + 1 # visited
                    #print('visited[%d][%d][0] = '%(nx, ny), 'visited[%d][%d][1]+1'%(x, y), ' = %d'%visited[nx][ny][0])
                    q.append((nx, ny, 0)) # 및 벽을 뚫었다는 0 상태를 큐에 추가하여 다음에 벽을 못뚫게함
                if graph[nx][ny] == 0 and visited[nx][ny][w] == 0: # 이동할 수 있고, 방문하지 않은 곳이라면
                    visited[nx][ny][w] = visited[x][y][w] + 1 # 이동 후 카운트 하기
                    #print('visited[%d][%d][%d] = '%(nx, ny, w), 'visited[%d][%d][%d]+1'%(x, y, w), ' = %d'%visited[nx][ny][w])
                    #print('w = ', w)
                    q.append((nx, ny, w))
    
    return -1
print(bfs())
