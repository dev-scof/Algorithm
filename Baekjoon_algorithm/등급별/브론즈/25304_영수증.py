total=int(input())
check=0
for _ in range(int(input())):
    a, b = map(int, input().split())
    check+=a*b
print('Yes') if total==check else print('No')