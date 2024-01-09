from itertools import combinations
for _ in range(int(input())):
    N, M = map(int, input().split())
    arr = [0] * M
    print(len(list(combinations(arr, N))))
import math
t = int(input())
for _ in range(t):
    n, m = map(int, input().split(' '))
    print(math.comb(m, n))