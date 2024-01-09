input()
ans=s=0
for i in sorted(map(int, input().split())):
    s+=i
    ans+=s
print(ans)