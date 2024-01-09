n, k = map(int, input().split())
for i in range(1, n+2):
    if n%i==0:
        k-=1
    if k==0:
        break
if i>n:
    print(0)
else:
    print(i)