n, k = map(int, input().split())
coins=[]
ans=0
for _ in range(n):
    coins.append(int(input()))
while k>0:
    if k>=coins[-1]:
        ans+=k//coins[-1]
        k-=k//coins[-1]*coins[-1]
    else:
        coins.pop()
print(ans)