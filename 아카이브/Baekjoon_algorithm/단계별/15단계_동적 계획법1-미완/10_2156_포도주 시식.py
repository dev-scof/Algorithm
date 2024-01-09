import sys
input = sys.stdin.readline

N = int(input())
dp = [0]*N
arr = []
for _ in range(N):
    arr.append(int(input()))

dp[0] = arr[0]
if N>1:
    dp[1] = arr[0]+arr[1]
if N>2:
    dp[2] = max(arr[0]+arr[2], arr[1]+arr[2], dp[1])

for i in range(3,N):
    '''
    arr[i] + dp[i-2] : 한칸 건너 뛰는 방법
    arr[i] + arr[i-1] + dp[i-3] : 연속 2번 먹는 방법
    dp[i-1] : 안먹는 방법
    '''
    dp[i]=max(arr[i]+dp[i-2], arr[i]+arr[i-1]+dp[i-3], dp[i-1])
print(dp)
print(max(dp))