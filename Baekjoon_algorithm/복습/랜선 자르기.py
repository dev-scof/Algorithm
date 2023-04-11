K, N = map(int, input().split())
arr = []
last = 0
for _ in range(K):
    num = int(input())
    if num > last:
        last=num
    arr.append(num)
def sol(s, l):
    if s>l:
        return l
    mid = (s+l)//2
    cnt=0
    for len in arr:
        cnt += len//mid
    if cnt>=N:
        return sol(mid+1, l)
    else:
        return sol(s, mid-1)
print(sol(1, last))