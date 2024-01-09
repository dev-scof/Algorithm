import sys
input = sys.stdin.readline
N=int(input())


dp=[0]*(N+1)

for i in range(2, N+1):
    ## 여기서 왜 if 1빼는 방법, 2 나누기, 3 나누기 동등하게 하지 않고 처음에 1을 빼고 시작하는지 의아해 할 수 있다.
    ## 1을 빼고 시작하는 이유는 다음에 계산할 나누기가 1을 뺀 값보다 작거나 큼에 따라 어차피 교체되기 때문이다.
    ## 즉 셋 다 시도하는 방법이 맞다.

    dp[i] = dp[i-1]+1
    if i%3==0:
        dp[i] = min(dp[i//3] + 1 , dp[i])
    elif i%2==0:
        dp[i] = min(dp[i//2] + 1, dp[i])
        
print(dp)