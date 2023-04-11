def ctor(n):
    sum=n
    while n:
        sum+=n%10
        n//=10
    return sum
n = int(input())
ctors=[]
for i in range(1, n+1):
    ctors.append(ctor(i))
    if ctor(i) == n:
        print(i)
        break
    if i==n:
        print(0)
print(ctors)