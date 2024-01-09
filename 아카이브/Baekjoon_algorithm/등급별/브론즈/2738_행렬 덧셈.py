n, m = map(int, input().split())
answer = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        answer[i][j]+=b[i][j]
for i in range(n):
    print(' '.join(map(str, answer[i])))