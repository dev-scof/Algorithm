import sys
input = sys.stdin.readline

N = int(input())
wines = []
dp = [0]*N
for _ in range(N):
    wines.append(int(input()))

# base case 초기화
dp[0] = wines[0]
if N>=2:
    dp[1] = wines[0]+wines[1]
if N>=3:
    dp[2] = max(wines[0]+wines[2], wines[1]+wines[2], dp[1])

for i in range(3, N):
    dp[i] = max(dp[i-2] + wines[i], dp[i-3] + wines[i-1] + wines[i], dp[i-1])
print(max(dp))