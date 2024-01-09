N = int(input())
video = [list(map(int, input())) for _ in range(N)]
result = []
def solution(x, y, N):
    color = video[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != video[i][j]:
                print('(', end='')
                solution(x, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
                print(')', end='')
                return
    print(color, end='')
solution(0,0,N)