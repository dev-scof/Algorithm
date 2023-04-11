'''
2023.03.08
- 5분 : 시간초과
- 10분 : 시간초과
- import sys -> 통과
'''
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
S=[0]
for i in range(1, N+1):
    S.append(S[i-1]+arr[i-1])
for _ in range(M):
    i, j = map(lambda x:int(x)-1, input().split())
    print(S[j+1]-S[i])