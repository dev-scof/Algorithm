from collections import deque
di = [0,0,1,-1]
dj = [1,-1,0,0]
store = dict()

def sol(idx, board):
    q = deque()
    q.append(idx)
    visited = dict()
    visited[idx]=0
    while q:
        cur_idx = q.popleft()
        # print(f'cur_idx({cur_idx})에서 시작')
        # 현재 이동 수
        cnt = visited[cur_idx[0], cur_idx[1]]+1
        if cur_idx[0]<0 or cur_idx[0]>=len(board) or cur_idx[1]<0 or cur_idx[1]>=len(board[0]):
            continue
        if board[cur_idx[0]][cur_idx[1]]=='G':
            # print('도달******************************************************************8888')
            # print("현재 cnt = ", cnt)
            return cnt-1
        if cur_idx in store:
            continue
        for k in range(4):
            i, j = cur_idx[0], cur_idx[1]
            while True:
                if i+di[k]<0 or i+di[k]>=len(board) or j+dj[k]<0 or j+dj[k]>=len(board[0]) or board[i+di[k]][j+dj[k]]=='D':
                    break
                if i+di[k]==cur_idx[0] and j+dj[k]==cur_idx[1]:
                    continue
                i+=di[k]
                j+=dj[k]
            i = i if i>0 else 0
            j = j if j>0 else 0
            i = i if i<len(board) else len(board)-1
            j = j if j<len(board[i]) else len(board)-1
            # print("****************")
            if (i, j) not in visited:
                visited[(i, j)]=cnt
                # print(f'({i, j}) 추가요')
                q.append((i, j))
            elif (i, j) in visited:
                if visited[(i, j)]>cnt:
                    # print(f"{i, j} {cnt}로갱신요")
                    visited[(i, j)] = cnt
                    q.append((i, j))

                
    #     print("현재 cnt = ", cnt)
    #     print('현재 queue = ', q)
    # for i in range(len(board)):
    #     for j in range(len(board[i])):
    #         print(f"{str(visited.get((i, j), '.')):3s}", end=' ')
    #     print()
    return False


def solution(board):
    answer = 0
    root_idx = None
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]=='R':
                root_idx = (i, j)
    res = sol(root_idx, board)
    if res==False:
        return -1
    else:
        return res

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))