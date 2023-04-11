n, m = map(int, input().split())
board1=[]
board2=[]
in_board = [list(input()) for _ in range(n)]
color=['W', 'B']

# 보드 생성
for i in range(n):
    line1 = []
    line2 = []
    c_idx=i%2
    for j in range(m):
        line1.append(color[c_idx%2]) # 처음이 흰색
        line2.append(color[(c_idx+1)%2])
        c_idx+=1
    board1.append(line1)
    board2.append(line2)
answer = n*m
def check_board(in_board, cur_i, cur_j):
    cnt1=cnt2=0
    for i in range(8):
        for j in range(8):
            if board1[i][j] != in_board[i+cur_i][j+cur_j]:
                cnt1+=1
            if board2[i][j] != in_board[i+cur_i][j+cur_j]:
                cnt2+=1
    
    return min(cnt1, cnt2)
for i in range(n-7):
    for j in range(m-7):
        answer = min(answer, check_board(in_board, i, j))
print(answer)
