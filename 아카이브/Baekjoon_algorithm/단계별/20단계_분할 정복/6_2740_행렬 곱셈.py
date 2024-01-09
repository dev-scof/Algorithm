import sys
input = sys.stdin.readline
a = []
b = []
ans = []
N, M = map(int, input().rstrip().split())
for _ in range(N):
    a.append(list(map(int, input().rstrip().split())))

M, K = map(int, input().rstrip().split())
for _ in range(M):
    b.append(list(map(int, input().rstrip().split())))

# A*B
for i in range(N):
    c = []
    for j in range(K):
        value = 0
        for k in range(M):
            value += a[i][k]*b[k][j]
        c.append(value)
    ans.append(c)


for i in range(N):
    for j in range(K):
        print(ans[i][j], end=' ')
    print()
