n, m = map(int, input().split())
a=list(range(1, n+1))
for _ in range(m):
    i, j = map(lambda x:x-1, map(int, input().split()))
    a = a[:i]+list(reversed(a[i:j+1]))+a[j+1:]
print(' '.join(map(str, a)))