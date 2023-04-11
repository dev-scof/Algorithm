cache=[[[0]*21 for _ in range(21)] for __ in range(21)]
def w(a, b, c):
    if a<=0 or b<=0 or c<=0:
        return 1
    if a>20 or b>20 or c>20:
        return w(20,20,20)
    # 캐시에 들어있을 경우 -> 캐시값 반환
    if cache[a][b][c]:
        return cache[a][b][c]
    
    if a<b<c:
        # 캐시에 저장 후 반환
        cache[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
        return cache[a][b][c]
    # 위의 조건이 아닐 경우
    # 새로 계산 후 캐시 반환
    cache[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return cache[a][b][c]

while True:
    a, b, c = map(int, input().split())
    if a==b==c==-1:
        break
    print('w(%d, %d, %d) = %d'%(a,b,c, w(a,b,c)))