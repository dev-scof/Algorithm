import copy
'''
접근 방법.
1. 잘못된 생각
- R, B는 센다
- G는 색약 정답에서는 세지 않는다.
-> G로만 구성된 경우, 색약의 수는 0이된다.

2. 정답
- 받은 리스트는 정상 그래프
- 받은 리스트에서 G를 R로 변경시킨 것은 색약 그래프로 나눈다.
dfs수행

'''

def dfs(i, j, color, visited, board):
    if i<0 or i>=N or j<0 or j>=N:
        return
    if board[i][j] != color:
        return
    if (i, j) not in visited:
        visited.add((i, j))
        for x in range(4):
            ni = di[x]+i
            nj = dj[x]+j
            dfs(ni, nj, color, visited, board)


N = int(input())
graph = [list(input()) for x in range(N)]
# 적록색양용 그래프
rg_graph = copy.deepcopy(graph)
for i in range(N):
    for j in range(N):
        if rg_graph[i][j]=='G':
            rg_graph[i][j]='R'
nor_visited=set()
rg_visited=set()
di = [0,0,1,-1]
dj = [1,-1,0,0]
answer = [0, 0]
for i in range(N):
    for j in range(N):
        # 정상
        if (i, j) not in nor_visited:
            dfs(i, j, graph[i][j], nor_visited, graph)
            answer[0]+=1
        # 적록색약
        if (i, j) not in rg_visited:
            dfs(i, j, rg_graph[i][j], rg_visited, rg_graph)
            answer[1]+=1
print(' '.join(map(str, answer)))