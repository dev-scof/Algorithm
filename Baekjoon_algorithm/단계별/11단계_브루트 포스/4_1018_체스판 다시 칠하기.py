def check_board(cur_i, cur_j, start_color):
    cnt=0
    row_color=''
    for i in range(cur_i, cur_i+8):
        # 첫 행의 첫번째 색깔 지정
        if row_color=='':
            row_color = start_color
        else:
            if row_color == 'W':
                row_color = 'B'
            else:
                row_color = 'W'
        color = row_color
        # 열을 돌면서 체크
        for j in range(cur_j, cur_j+8):
            if color != chess[i][j]:
                cnt+=1
            # 색깔 변경
            if color == 'W':
                color = 'B'
            else:
                color = 'W'
    return cnt
N, M = map(int, input().split())
chess = [list(input()) for _ in range(N)]
answer=check_board(0,0,'W')
for i in range(N-7):
    for j in range(M-7):
        w = check_board(i,j,'W')
        b = check_board(i,j,'B')
        if w < answer:
            answer=w
        if b < answer:
            answer=b
print(answer)