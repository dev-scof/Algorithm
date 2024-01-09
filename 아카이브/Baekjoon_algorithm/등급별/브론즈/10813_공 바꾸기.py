n, m = map(int, input().split())
a = list(range(1, n+1))
for _ in range(m):
    i, j = map(lambda x:x-1, map(int, input().split()))
    a[i], a[j] = a[j], a[i]
print(' '.join(map(str, a)))