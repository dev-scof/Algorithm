'''
dp[1] = 1
dp[2] = 3
dp[3] = 5
dp[4] = 
'''
n = int(input())
dp = [1, 3, 5]
for i in range(len(dp), n):
    dp.append(dp[i-1] + (dp[i-2])*2)
print(dp[n-1]%10_007)