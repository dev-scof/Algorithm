'''
https://lbdiaryl.tistory.com/167
'''
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))

dp1 = [1]*N
dp2 = [1]*N
# 가장 긴 증가하는 부분 수열
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)

arr.reverse()
# 오른쪽에서 가장 긴 증가하는 부분 수열
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)
dp2.reverse()
result = list(map(lambda x,y:x+y, dp1, dp2))
print(max(result)-1)