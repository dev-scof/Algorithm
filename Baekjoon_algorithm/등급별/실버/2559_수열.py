import sys
input = sys.stdin.readline
N, K = map(int, input().split())
days = list(map(int, input().split()))
answer = sum(days[:K])
dp = [answer]
for i in range(1, N-K+1):
    s = dp[i-1]-days[i-1]+days[i+K-1]
    if s>answer:
        answer=s
    dp.append(s)
print(answer)