N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
result = [0, 0]
def solution(x, y, N):
    color = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]:
                solution(x, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
                return
    result[color]+=1

solution(0, 0, N)
for ans in result:
    print(ans)