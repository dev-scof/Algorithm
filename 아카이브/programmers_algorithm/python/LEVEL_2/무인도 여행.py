'''
지도에는 바다와 무인도들에 대한 정보가 표시되어있다.
X또는 1~9 사이의 자연수가 적혀있다.
X : 바다
숫자 : 무인도, 식량 수

상,하,좌,우로 연결되는 땅은 하나의 무인도를 이룬다.

'''
import sys
sys.setrecursionlimit(10000)
def show_board(board):
    for line in board:
        print(line)
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
def dfs(idx, board, cnt):
    board[idx[0]][idx[1]]=-1
    for k in range(4):
        ni = idx[0]+di[k]
        nj = idx[1]+dj[k]
        if ni<0 or nj<0 or ni>=len(board) or nj>=len(board[0]):
            continue
        if board[ni][nj] != -1:
            cnt+=dfs((ni,nj), board, board[ni][nj])
    return cnt
def solution(maps):
    answer = []
    board = []
    visited = set()
    for i in range(len(maps)):
        temp = []
        for j in range(len(maps[i])):
            if maps[i][j] == 'X':
                temp.append(-1)
            else:
                temp.append(int(maps[i][j]))
        board.append(temp)
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (i, j) not in visited and board[i][j] != -1:
                answer.append(dfs((i, j), board, board[i][j]))
    
    if answer:
        return list(sorted(answer))
    else:
        return [-1]

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))
print(solution(["XXX","XXX","XXX"]))