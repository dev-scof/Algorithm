T = int(input())
'''
dp[0] = fibo(0) => (1, 0) // 0 한번
dp[1] = fibo(1) => (0, 1) // 1 한번
dp[2] = fibo(1)+fibo(0) => (1, 1)
dp[3] = fibo(1)+fibo(2) => fibo(1)+fibo(1)+fibo(0) => dp[2]+dp[1] // (1, 2)
...

'''
dp = [(1, 0), (0, 1)]

for _ in range(T):
    N = int(input())
    for i in range(len(dp), N+1):
        dp.append((dp[i-2][0]+dp[i-1][0], dp[i-2][1]+dp[i-1][1]))
    print(' '.join(map(str, dp[N])))