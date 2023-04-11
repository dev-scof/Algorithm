'''
https://cotak.tistory.com/12


풀이)
- 0을 제외한 모든 숫자는 앞에 올 수 있다.
- 이때 1~8은 뒤에 올 수 있는 숫자가 총 2종류이다(숫자±1).
- 하지만 9 뒤엔 오직 숫자 8만이 올 수 있다.

'''
import sys
input = sys.stdin.readline

N = int(input())
dp = [[0]*10 for _ in range(N+1)]

for i in range(1, 10):
    dp[1][i] = 1

# 2부터 N+1의 길이까지 반복
for i in range(2, N+1):
    for j in range(10):
        if j==0:
            dp[i][j] = dp[i-1][1]
        elif j==9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(dp)
print(sum(dp[N]) %  1_000_000_000)

