n = int(input())
m = int(input())
INF = int(1e9)

# 2차원 테이블 생성 및 INF로 초기화
floyd_table = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용을 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            floyd_table[a][b] = 0

# 입력받은 값으로 초기화
for _ in range(m):
    # a에서 b로 가는 비용이 c
    a, b, c = map(int, input().split())
    floyd_table[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
def floyd_warshall():
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                # a : 출발노드, k : 거쳐가는 노드, b : 도착노드
                floyd_table[a][b] = min(floyd_table[a][b], floyd_table[a][k] + floyd_table[k][b])

floyd_warshall()
for a in range(1, n+1):
    for b in range(1, n+1):
        if floyd_table[a][b]==INF:
            print('0', end=' ')
        else:
            print(floyd_table[a][b], end=' ')
    print()