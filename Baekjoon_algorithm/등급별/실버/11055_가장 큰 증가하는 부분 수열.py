from bisect import bisect_left
import sys
input = sys.stdin.readline
N = input()
A = list(map(int, input().split()))
dp = [0]
for a in A:
    if dp[-1] < a:
        dp.append(a)
        continue
    idx = bisect_left(dp, a)
    dp[idx] = a

print(len(dp)-1)