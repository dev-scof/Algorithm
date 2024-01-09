# review 필요
import sys
input = sys.stdin.readline
N = int(input())
dp = []
for _ in range(N):
    dp.append(list(map(int, input().split())))
print(dp)
for i in range(1, len(dp)):
    # i번째집을 빨강으로 칠했을 때의 최솟값
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0]

    # i번째집을 초록으로 칠했을 때의 최솟값
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + dp[i][1] 
    
    # i번째집을 파랑으로 칠했을 때의 최솟값
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + dp[i][2] 
    print('수정된 dp = ', dp)
print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))