import sys
input = sys.stdin.readline
K, N = map(int, input().split())
arr = []
last=0
for _ in range(K):
    num = int(input())
    if last<num:
        last=num
    arr.append(num)

def lan(s, l):
    if s>l:
        return l
    m = (s+l)//2
    cnt=0
    for num in arr:
        cnt+=num//m
    if cnt>=N:
        return lan(m+1, l)
    else:
        return lan(s, m-1)

print(lan(1, last))