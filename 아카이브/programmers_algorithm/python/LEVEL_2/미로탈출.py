def show_board(board):
    for line in board:
        print(line)
from collections import deque

def bfs(start, end, board):
    queue = deque([start])
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    visited=set()
    while queue:
        for q in range(len(queue)):
            cur = queue.popleft()
            visited.add(cur)
            for k in range(4):
                ni = cur[0]+di[k]
                nj = cur[1]+dj[k]
                if ni<0 or nj<0 or ni>=len(board) or nj>=len(board[0]):
                    continue
                if (ni,nj) not in visited and board[ni][nj]!=-1:
                    queue.append((ni, nj))
                    visited.add((ni, nj))
                    board[ni][nj]=board[cur[0]][cur[1]]+1
                    if (ni, nj) == end:
                        return True
    return False

def solution(maps):
    board = []
    for i in range(len(maps)):
        temp = []
        for j in range(len(maps[i])):
            if maps[i][j]=='O':
                temp.append(0)
            elif maps[i][j]=='S':
                start = (i, j)
                temp.append(0)
            elif maps[i][j]=='L':
                temp.append(0)
                lever = (i, j)
            elif maps[i][j]=='E':
                end = (i, j)
                temp.append(0)
            else:
                temp.append(-1)
        board.append(temp)
    if bfs(start, lever, board):
        if bfs(lever, end, board):
            return board[end[0]][end[1]]
    return -1

print(solution(
    [
        "SOOOL",
        "XXXXO",
        "OOOOO",
        "OXXXX",
        "OOOOE"
    ]))
print(solution(
    [
        "SOOOL",
        "OXXXO",
        "OOOOO",
        "OXXXX",
        "OOOOE"
    ]))
print(solution(
    [
        "LOOXS",
        "OOOOX",
        "OOOOO",
        "OOOOO",
        "EOOOO"
    ]))