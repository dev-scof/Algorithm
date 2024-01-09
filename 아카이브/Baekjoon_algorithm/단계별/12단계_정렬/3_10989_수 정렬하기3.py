from sys import stdin
from collections import Counter
input = stdin.readline
n=int(input())
numbers=Counter()
for _ in range(n):
    numbers[int(input())]+=1
for num, cnt in sorted(numbers.items(), key=lambda x:x[0]):
    for _ in range(cnt):
        print(num)
