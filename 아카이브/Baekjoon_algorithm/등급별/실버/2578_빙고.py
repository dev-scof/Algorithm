idx={}
board=[]
for _ in range(5):
    board.append(list(map(int, input().split())))
for i in range(5):
    for j in range(5):
        idx[board[i][j]]=(i, j)
calls=[]
for _ in range(5):
    calls+=list(map(int, input().split()))
def check_bingo():
    cnt=0
    # 가로 빙고
    for i in range(5):
        S=0
        for j in range(5):
            S+=board[i][j]
        if S==0:
            cnt+=1
    # 세로 빙고
    for j in range(5):
        S=0
        for i in range(5):
            S+=board[i][j]
        if S==0:
            cnt+=1
    # 대각선 빙고
    if board[0][0]==board[1][1]==board[2][2]==board[3][3]==board[4][4]:
        cnt+=1
    if board[4][0]==board[3][1]==board[2][2]==board[1][3]==board[0][4]:
        cnt+=1
    return cnt

for index, call in enumerate(calls):
    i, j = idx.get(call)
    board[i][j]=0
    if check_bingo()>=3:
        print(index+1)
        break
