from pprint import pprint

def rotate_90(board):
    n = len(board)
    # 새로운 배열 생성
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[j][n-1-i] = board[i][j]
    return res
def rotate_180(board):
    n = len(board)
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[n-1-i][n-1-j] = board[i][j]
    return res

def rotate_270(board):
    n = len(board)
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[n-1-j][i] = board[i][j]
    return res

board = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
pprint(board, width=20)
print()
pprint(rotate_90(board), width=20)
print()
pprint(rotate_180(board), width=20)
print()
pprint(rotate_270(board), width=20)