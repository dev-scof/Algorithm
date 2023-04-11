n, m = map(int, input().split())
a = list(range(1, n+1))
for _ in range(m):
    i, j, k = map(lambda x:int(x)-1, input().split())
    a = a[:i]+a[k:j+1]+a[i:k]+a[j+1:]
print(' '.join(map(str, a)))

