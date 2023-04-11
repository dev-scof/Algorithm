def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
m=int(input())
n=int(input())
ans1=n
ans2=0
for i in range(m, n+1):
    if is_prime(i):
        if i<ans1:
            ans1=i
        ans2+=i
if ans2==0:
    print(-1)
else:
    print(ans2)
    print(ans1)