n = int(input())
'''
1 => 1개
2 => 2개
3 => 3개
4 => 5개
5 => 8개
...
dp[i] = dp[i-2]+dp[i-1]
'''
dp = [1, 2, 3]
for i in range(len(dp), n+1):
    dp.append(dp[i-2]+dp[i-1])
print(dp[n-1]%10_007)