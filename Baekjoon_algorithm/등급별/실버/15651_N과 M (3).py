from itertools import product
n, m = map(int, input().split())
answer = list(sorted(product(range(1, n+1), repeat=m), key=lambda x:x[0]))
for ans in answer:
    print(' '.join(map(str, ans)))