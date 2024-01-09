'''
강의 서쪽 N개의 사이트
강의 동쪽 M개의 사이트
서쪽의 사이트와 동쪽의 사이트를 연결
-> 조합 combination
-> mCn -> m!/(m-n)!*n!
'''
TC = int(input())
for i in range(TC):
    n, m = map(int, input().split())
    if n==m:
        print('1')
    else:
        up = down = 1
        for j in range(n+1, m+1):
            up*=j
        for j in range(1, m-n+1):
            down*=j
        print(up//down)