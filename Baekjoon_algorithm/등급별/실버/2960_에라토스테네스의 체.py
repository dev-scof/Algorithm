n, k = map(int, input().split())
numbers=list(range(n, 1, -1))
ans=0
while numbers != []:
    p = numbers[-1]
    for num in numbers[::-1]:
        if num%p==0:
            ans=numbers.pop(numbers.index(num))
            k-=1
        if k==0:
            break
    if k==0:
        break
print(ans)