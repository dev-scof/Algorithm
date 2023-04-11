n = int(input())
a = list(sorted(map(int, input().split())))
for i in range(n):
    print('a i = ', a[i])
    for j in (n-1, i, -1):
        print(a[j], end=' ')
    print()
print(a)