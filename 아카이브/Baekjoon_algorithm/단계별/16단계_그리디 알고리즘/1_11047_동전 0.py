N, K = map(int, input().split())
coins=[int(input()) for _ in range(N)]
idx=len(coins)-1
cnt=0
while idx>=0:
    if K-coins[idx]>=0:
        K-=coins[idx]
        cnt+=1
    else:
        idx-=1
print(cnt)