n = int(input())
m = int(input())
INF = int(1e9)
floyd_table = [[INF]*(n+1) for _ in range(n+1)]
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            floyd_table[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if floyd_table[a][b] > c:
        floyd_table[a][b] = c

def floyd_warshall():
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                floyd_table[a][b] = min(floyd_table[a][b], floyd_table[a][k]+floyd_table[k][b])

floyd_warshall()
for a in range(1, n+1):
    for b in range(1, n+1):
        if floyd_table[a][b]==INF:
            print('0', end=' ')
        else:
            print(floyd_table[a][b], end=' ')
    print()