# n!/k!*(n-k)!을 정리
n, k = map(int, input().split())
if k<0 or k>n:
    print(0)
else:
    up_fac=down_fac=1
    for i in range(n-k+1, n+1):
        up_fac*=i
    for i in range(1, k+1):
        down_fac*=i
    print((up_fac//down_fac)%1_0007)
