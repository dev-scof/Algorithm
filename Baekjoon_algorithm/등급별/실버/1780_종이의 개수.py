N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]
result=[0, 0, 0]
def solution(x, y, N):
    color=papers[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != papers[i][j]:
                next_N = N//3
                solution(x, y, next_N)
                solution(x, y+ next_N, next_N)
                solution(x, y+ next_N*2, next_N)
                
                solution(x+next_N, y, next_N)
                solution(x+next_N, y+next_N, next_N)
                solution(x+next_N, y+next_N*2, next_N)

                solution(x+next_N*2, y, next_N)
                solution(x+next_N*2, y+next_N, next_N)
                solution(x+next_N*2, y+next_N*2, next_N)
                return
    result[color]+=1
solution(0, 0, N)
for i in range(-1, 2):
    print(result[i])