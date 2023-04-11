n = int(input())
data = [int(input()) for _ in range(n)]
data.sort()
print('\n'.join(map(str, data)))