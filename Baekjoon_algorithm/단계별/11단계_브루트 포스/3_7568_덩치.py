n = int(input())
P = []
for _ in range(n):
    P.append(tuple(map(int, input().split())))
for i in range(n):
    rank=1 # 1부터 시작
    for j in range(n):
        rank += 1 if P[i][0] < P[j][0] and P[i][1] < P[j][1] else 0
    print(rank, end=' ')