dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
T = int(input())
for _ in range(T):
    N = int(input())
    for i in range(len(dp), N+1):
        dp.append(dp[len(dp)-1]+dp[len(dp)-5])
    print(dp[N])