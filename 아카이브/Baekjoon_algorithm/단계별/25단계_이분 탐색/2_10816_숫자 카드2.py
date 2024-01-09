from collections import Counter
import sys
input = sys.stdin.readline
input()
count = Counter(map(int, input().rstrip().split()))
input()
for i in map(int, input().rstrip().split()):
    print(count[i], end=' ') if i in count else print(0, end=' ')