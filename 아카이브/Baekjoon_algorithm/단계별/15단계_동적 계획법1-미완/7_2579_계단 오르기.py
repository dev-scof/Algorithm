'''
steps[i] : 주어진 점수 데이터
dp[i] : i번째까지의 최대 점수

# base case
dp[0] : 0번째까지의 최대 점수 = steps[0]
dp[1] : 1번째까지의 최대 점수
    - [0]을 거쳐서 가는 방법 -> steps[0]+steps[1]
    - [0]을 거치지 않는 방법 -> steps[1]

# CASE
dp[i] : i번째까지의 최대 점수
    - [i-1]을 거쳐서 가는 방법 -> dp[i-3]+steps[i-1]+steps[i]
    - [i-1]을 거치지 않는 방법 -> dp[i-2]+steps[i]

'''
import sys
input = sys.stdin.readline

N = int(input())
steps = [0]*N
dp = [0]*N
for _ in range(N):
    steps[_] = int(input())

# base case 초기화
dp[0] = steps[0]
if N>=2:
    dp[1] = max(steps[1], steps[0]+steps[1])
if N>=3:
    dp[2] = max(steps[0]+steps[2], steps[1]+steps[2])

for i in range(3, N):
    dp[i] = max(dp[i-2] + steps[i], dp[i-3] + steps[i-1] + steps[i])
print(dp)