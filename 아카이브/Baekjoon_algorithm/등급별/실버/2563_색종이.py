pos = [[0]*100 for _ in range(100)]
n = int(input())
answer=0
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, min(x+10, 100)):
        for j in range(y, min(y+10, 100)):
            pos[i][j]=1
for i in range(100):
    answer+=sum(pos[i])
print(answer)