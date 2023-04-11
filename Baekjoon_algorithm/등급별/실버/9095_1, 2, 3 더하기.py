T = int(input())
'''
1 -> 1
2 -> 1+1, 2   = 2
3 -> 1+1+1, 1+2, 2+1, 3 = 4
4 -> 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1 = 7
5
 -> dp[4]에 1을 붙인 것 -> dp[4]
 -> dp[3]에 2를 붙인 것 -> dp[3]
 -> dp[2]에 3을 붙인 것 -> dp]2]
'''
dp = [0, 1, 2, 4]
for _ in range(T):
    N = int(input())
    if N >= len(dp):
        for i in range(len(dp), N+1):
            dp.append(dp[i-1]+dp[i-2]+dp[i-3])
    print(dp[N])
