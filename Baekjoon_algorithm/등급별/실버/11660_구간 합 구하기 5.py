'''
x1, y1 ~ x2, y2까지으 합을 구하기

'''
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
answer = dict()
for _ in range(N):
    arr.append(list(map(int, input().split())))
                
for k in range(N):
    for l in range(N):
        if (k-1, l) in answer:
            answer[(k, l)] = answer[(k-1, l)]+sum(arr[k][:l+1])
        else:
            answer[(k, l)] = sum(arr[k][:l+1])

for _ in range(M):
    x1, y1, x2, y2 = map(lambda x:x-1, map(int, input().split()))
    if x1==y1==0:
        print(answer[x2, y2])
    else:
        temp = answer[x2, y2]
        if y1!=0:
            temp -= answer[x2, y1-1]
        if x1!=0:
            temp -= answer[x1-1, y2]
        if x1!=0 and y1!=0:
            temp += answer[x1-1, y1-1]
        print(temp)