def recursive_fibo(a, b, n):
    if n==0:
        return a
    t = a
    a = b
    b = b+t
    return recursive_fibo(a, b, n-1)
n = int(input())
print(recursive_fibo(0, 1, n))


# 방법 2 : 재귀 + dp
dp = [0]*100
def fibo(x):
    if x==1 or x==2:
        return 1
    if dp[x] != 0: #이미 계산되었다면
        return dp[x]
    dp[x] = fibo(x-1) + fibo(x-2)
    return dp[x]