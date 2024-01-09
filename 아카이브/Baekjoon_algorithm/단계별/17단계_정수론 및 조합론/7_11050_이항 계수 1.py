# dp 사용
n, k = map(int, input().split())
dp = [1]
def factorial(n) -> int:
    if n>=len(dp):
        for i in range(len(dp), n+1):
            dp.append(dp[-1]*i)
    return dp[n]
print(int(factorial(n)/(factorial(k)*factorial(n-k))))