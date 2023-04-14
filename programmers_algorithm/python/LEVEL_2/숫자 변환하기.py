'''
X에 n곱하기
x에 2곱하기
x에 3곱하기

DP네
'''
from collections import deque
def solution(x, y, n):
    INF = 1e9
    max_num = 1_000_000
    dp = [INF]*(max_num*4)
    dp[x]=0
    queue = deque([x])
    while queue:
        x = queue.popleft()
        if x>max_num:
            continue
        if dp[x+n] > dp[x]+1:
            dp[x+n]=dp[x]+1
            queue.append(x+n)
        if dp[2*x] > dp[x]+1:
            dp[2*x]=dp[x]+1
            queue.append(2*x)
        if dp[3*x] > dp[x]+1:
            dp[3*x]=dp[x]+1
            queue.append(3*x)
    
    if dp[y]==INF:
        return -1
    return dp[y]

print(solution(10, 40, 5))
print(solution(10, 40, 30))
print(solution(2, 5, 4))