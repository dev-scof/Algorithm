V, E = map(int, input().split())
INF = int(1e9)
table = [[INF]*(V+1) for _ in range(V+1)]

# 테이블 초기화
for a in range(V+1):
    for b in range(V+1):
        if a==b:
            table[a][b] = 0
for _ in range(E):
    a, b, c = map(int, input().split())
    if table[a][b] > c:
        table[a][b] = c
# 플로이드 워셜
for k in range(1, V+1):
    for a in range(1, V+1):
        for b in range(1, V+1):
            table[a][b] = min(table[a][b], table[a][k]+table[k][b])

# 비용 계산
answer = INF
for a in range(1, V+1): # a에서 시작
    cost = 0
    for b in range(1, V+1): # b를 거쳐 a로 가는 것
        if a==b: # 자기 자신을 찍는 경우는 제외
            continue
        cost = table[a][b] + table[b][a]
        if cost<answer:
            answer = cost
if answer>=INF:
    print(-1)
else:
    print(answer)