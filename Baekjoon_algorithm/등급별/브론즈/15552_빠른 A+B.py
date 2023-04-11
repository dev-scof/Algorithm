import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a, b = map(int, input().rstrip().split())
    print(a+b)