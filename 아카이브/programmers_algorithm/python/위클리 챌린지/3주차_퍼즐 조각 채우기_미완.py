def shape(board, cur_i, cur_j, num): 
    if cur_i>=len(board) and cur_j>=len(board):
        return 0
    

def solution(game_board, table):
    blank = []
    row = col = len(game_board)
    for i in range(row):
        for j in range(col):
            if game_board[i][j] == 0:
                pass
    print(blank)

print(solution(
    [
        [1,1,0,0,1,0],
        [0,0,1,0,1,0],
        [0,1,1,0,0,1],
        [1,1,0,1,1,1],
        [1,0,0,0,1,0],
        [0,1,1,1,0,0]
    ], 
    [
        [1,0,0,1,1,0],
        [1,0,1,0,1,0],
        [0,1,1,0,1,1],
        [0,0,1,0,0,0],
        [1,1,0,1,1,0],
        [0,1,0,0,0,0]
    ]
))