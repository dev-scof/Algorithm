'''
말은 상하좌우로, 인접한 테 칸중 한칸으로 이동,
같은 알파벳이 적힌 칸을 두번 지날 수 없다.
-> dfs
'''
import sys
input = sys.stdin.readline
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
visited=[False for x in range(26)]
di = [0,0,1,-1]
dj = [1,-1,0,0]
answer = 0
def dfs(i, j, cnt):
    global answer
    if cnt>answer:
        answer=cnt

    visited[ord(board[i][j])-ord('A')]=True
    print(f'({i, j}) 방문')
    for k in range(4):
        ni = i+di[k]
        nj = j+dj[k]
        if ni<0 or ni>=R or nj<0 or nj>=C:
            continue
        if visited[ord(board[ni][nj])-ord('A')]:
            continue
        dfs(ni, nj, cnt+1)
        visited[ord(board[ni][nj])-ord('A')]=False
    
dfs(0,0,0)
print(answer)
'''
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]

answer = 0
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def dfs() :
    global answer
    stack = set([(0, 0, board[0][0])])
    while stack :
        x, y, alph = stack.pop()
        answer = max(answer, len(alph))
        if answer == 26 :
            break
        for dx, dy in dxy :
            nx = x + dx
            ny = y + dy
            if 0 <= nx < r and 0<= ny < c and board[nx][ny] not in alph :         
                stack.add((nx, ny, alph + board[nx][ny]))
dfs()
print(answer)
'''