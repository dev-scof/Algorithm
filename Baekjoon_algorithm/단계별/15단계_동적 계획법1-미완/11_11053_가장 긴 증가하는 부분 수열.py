'''
https://lbdiaryl.tistory.com/166
'''
from bisect import bisect_left
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().rsplit()))
answer = []
cnt = 0

for a in arr:

    # answer이 비어있으면 -> 삽입
    if not answer:
        cnt+=1
        answer.append(a)
        continue

    
    # answer의 마지막 값보다 a가 클경우 -> 마지막에 삽입
    if answer[-1] < a:
        cnt+=1
        answer.append(a)

    # answer의 마지막 값보다 a가 작을 경우
    # answer에서 a의 위치를 찾아 그 위치에 바꿔치기한다.
    else:
        idx = bisect_left(answer, a)
        answer[idx] = a

print(cnt)
'''
LIS 풀이

N = int(input())

List = list(map(int, input().split()))

dp = [1]*1000

for i in range(N):
    for j in range(i):
        if List[i] > List[j]:
            dp[i] = max(dp[i], dp[j]+1)
            
print(max(dp))
'''