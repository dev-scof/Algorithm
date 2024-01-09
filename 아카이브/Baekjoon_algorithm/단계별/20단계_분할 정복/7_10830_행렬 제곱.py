import sys
input = sys.stdin.readline

N, B = map(int, input().rstrip().split())
arr = []
ans = []
for _ in range(N):
    arr.append(list(map(int, input().rstrip().split())))

