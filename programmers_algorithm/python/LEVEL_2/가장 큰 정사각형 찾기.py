def solution(board):
    row = len(board)
    col = len(board[0])
    answer=0
    i=j=1
    if(row <= 1 or col <= 1) :
        return 1
    while i<row:
        if board[i][j]:
            up = board[i-1][j]
            left = board[i][j-1]
            upleft = board[i-1][j-1]
            Min = min(up, left, upleft)
            board[i][j] = Min +1
            answer = max(answer, Min+1)
        if j<col-1:
            j+=1
        else:
            j=1
            i+=1
            
    return answer**2
print(
    solution([
        [1,1,0,0,1,1,1,1],
        [1,1,1,0,1,1,1,1],
        [1,1,1,1,1,1,1,1], 
        [0,0,1,0,1,1,1,1]
    ])
)
'''
[0,1,1,1], 3
[1,1,1,1], 4
[1,1,1,1], 4
[0,0,1,0]  1
-> 9

[1,1,1,0], 3
[1,1,1,1], 4
[1,1,1,1], 4
[1,0,1,1]  3
-> 9

[0,1,1,0],
[1,1,1,0],
[1,1,1,1],
[0,0,1,0]
-> 4

[0,1,0,0],
[1,1,1,0],
[1,1,1,1],
[0,0,1,0]
-> 4

[1,1,0,0,1,1,1,1], -> 0 1 4 5 6 7
[1,1,1,0,1,1,1,1], -> 0 1 2 4 5 6 7
[1,1,1,1,1,1,1,1], -> 0 1 2 4 5 6 7 
[0,0,1,0,1,1,1,1]  -> 2 4 5 6 7
->16


'''