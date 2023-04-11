from sys import stdin
n = int(stdin.readline())
words = [input() for _ in range(n)]
words = sorted(list(set(words)))
for i in sorted(words, key=lambda x:(len(x))):
    print(i)