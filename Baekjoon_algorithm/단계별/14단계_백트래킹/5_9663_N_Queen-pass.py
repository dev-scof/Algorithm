from sys import stdin
# https://www.youtube.com/watch?v=z4wKvYdd6wM 참고
'''
방법
  조건
  - 같은 행에는 퀸을 놓지 않는다.
  구현
  - 유망 조건 따지기
'''
N = int(stdin.readline())
board = [0]*15
cnt=0
def is_valid(col):
    for i in range(col):
        if board[col] == board[i]: # 같은 열에 배치되어있을 경우 -> non valid
            return 0
        elif abs(col-i) == abs(board[col]-board[i]): # 같은 대각선 상에 있는 경우 -> non valid 
            return 0
    return 1

def N_Queen(depth):
    global cnt
    if depth == N:
        cnt+=1
        return
    for i in range(N):
        board[depth] = i # depth행 i열에 퀸을 둠
        if is_valid(depth):
            N_Queen(depth+1)

N_Queen(0)
print(cnt)

'''
이런 **... 답이 정해져있어서 아래와 같은 코드 작성이 가능하다;

a = (0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596)
print(a[int(input())])
'''