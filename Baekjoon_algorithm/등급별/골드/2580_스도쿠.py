board = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
flag=False
def is_promising(i, j):
    promising = [1,2,3,4,5,6,7,8,9] 
    # 행열 검사
    for k in range(9):
        if board[i][k] in promising:
            promising.remove(board[i][k])
        if board[k][j] in promising:
            promising.remove(board[k][j])
    # 3*3 박스 검사
    i//=3
    j//=3
    for p in range(i*3, i*3+3):
        for q in range(j*3, j*3+3):
            if board[p][q] in promising:
                promising.remove(board[p][q])
    return promising
def solution(depth):
    # 그만 찾아도 되면 탐색 중지
    global flag
    if flag:
        return
    if depth == len(zeros):
        for row in board:
            print(' '.join(map(str, row)))
        flag=True
        return
    i, j = zeros[depth]
    nums = is_promising(i, j)

    for num in nums:
        board[i][j]=num
        solution(depth+1)
        board[i][j]=0
solution(0)

