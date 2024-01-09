from collections import Counter
n, m = map(int, input().split())
answer=[0]*n
for _ in range(m):
    i, j, k = map(int, input().split())
    for l in range(i, j+1):
        answer[l-1]=k
print(' '.join(map(str, answer)))
