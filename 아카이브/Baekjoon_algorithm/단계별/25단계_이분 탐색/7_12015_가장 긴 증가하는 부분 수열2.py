from bisect import bisect_left
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().rsplit()))
answer = []
cnt = 0

for a in arr:

    if not answer:
        # answer에 없을 경우 -> 삽입
        cnt+=1
        answer.append(a)
        continue

    # answer에 있음

    # answer의 마지막 값보다 a가 클경우 -> 마지막에 삽입
    if answer[-1] < a:
        cnt+=1
        answer.append(a)

    # answer의 마지막 값보다 a가 작을 경우
    else:
        idx = bisect_left(answer, a)
        answer[idx] = a

print(cnt)