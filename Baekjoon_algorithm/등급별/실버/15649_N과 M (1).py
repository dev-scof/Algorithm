from itertools import permutations
n, m = map(int, input().split())
answer = list(sorted(permutations(range(1, n+1), m), key=lambda x:x[0]))
for ans in answer:
    print(' '.join(map(str, ans)))