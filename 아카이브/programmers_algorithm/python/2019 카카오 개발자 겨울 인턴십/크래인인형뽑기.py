def solution(board, moves):
    '''
    board는 2차원배열로 5*5, 30*30 이하
    board의 값 
        - 0 : 빈 칸
        - 1~100 : 각기 다른 인형의 모양

    moves는 1~1000의 배열
    moves의 값
        - 1이상, board의 가로 크기 이하의 자연수
    '''
    answer = 0
    stack = []
    board_line = len(board)
    print()
    
    for i in moves: # moves를 다할 때까지 반복
        line = 0
        while line <= board_line:
            if not board[board_line-1][i-1] : # 맨 아래의 값이 0일 경우 break
                break
            if not board[line][i-1] : # 현재 라인에 인형이 없을 경우 한번더 이동
                line += 1
            else : # 인형이 있을 경우, 인형을 스택에 넣고, 중지
                if len(stack) == 0 or stack[0] != board[line][i-1]:
                    stack.insert(0, board[line][i-1])
                else :
                    stack.pop(0)
                    answer +=2
                board[line][i-1] = 0
                break
    return answer
print(solution([
        [0,0,0,0,0], # board[0]
        [0,0,1,0,3], # board[1]
        [0,2,5,0,1], # board[2]
        [4,2,4,4,2], # board[3]
        [3,5,1,3,1] # board[4]
    ], [1,5,3,5,1,2,1,4]))
    