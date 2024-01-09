'''
    1. 가로, 세로, 대각선으로 3개가 같은 표시가 만들어지면, 표시를 만든 사람이 승리
    2. 9칸이 다 차면 무승부

    실수
    - "O"를 표시할 차례인데 "X"를 표시하거나 / 반대로 "X"를 표시할 차례인데 "O"를 표시한다.
    - 선공이나 후공이 승리해서 게임이 종료되었음에도 그 게임을 진행한다.
'''
def solution(board):
    answer = -1
    O = set()
    X = set()
    for i in range(3):
        for j in range(3):
            if board[i][j]=='O':
                O.add((i, j))
            elif board[i][j]=='X':
                X.add((i, j))
    
    if len(O) < len(X) or abs(len(O)-len(X)) >= 2:
        # X가 O보다 많거나 / 차이가 2개이상 나거나
        return 0
    if len(O)==len(X)==1:
        return 1
    bingo = [0, 0]
    # 빙고 체크
    for i in range(3):
        for j in range(3):
            # i, j에 대해 빙고 체크
            if board[i][j]=='O':
                flag = True
                # 세로 확인
                for k in range(3):
                    if board[k][j]!='O':
                        flag=False

                if flag:
                    bingo[0]+=1

                flag = True
                # 가로 확인
                for k in range(3):
                    if board[i][k]!='O':
                        flag=False
                if flag:
                    bingo[0]+=1

                # 대각선 하단 확인
                if board[0][0]==board[1][1]==board[2][2]=='O':
                    bingo[0]+=1
                # 대각선 상단 확인
                if board[2][0]==board[1][1]==board[0][2]=='O':
                    bingo[0]+=1

            if board[i][j] == 'X':
                flag = True
                # 세로 확인
                for k in range(3):
                    if board[k][j]!='X':
                        flag=False

                if flag:
                    bingo[1]+=1

                flag = True
                # 가로 확인
                for k in range(3):
                    if board[i][k]!='X':
                        flag=False
                if flag:
                    bingo[1]+=1

                # 대각선 하단 확인
                if board[0][0]==board[1][1]==board[2][2]=='X':
                    bingo[1]+=1
                # 대각선 상단 확인
                if board[2][0]==board[1][1]==board[0][2]=='X':
                    bingo[1]+=1
    
    # 빙고가 없을 때
    if bingo[0]==bingo[1]==0:
        return 1

    # O가 X보다 빙고가 많을 때
    if bingo[0] >= bingo[1]:
        if len(O)>bingo[0] or len(X)>=len(O):
            return 0
    # X가 더 많을 때
    elif bingo[1] > bingo[0]:
        if len(X)>bingo[1] or len(O) > len(X):
            return 0
    return 1

# print(solution(["O.X", ".O.", "..X"]))
# print(solution(["OOO", "...", "XXX"]))
# print(solution(["...", ".X.", "..."]))
# print(solution(["...", "...", "..."]))
print(solution(["OXX","XOX", "OOO"]))