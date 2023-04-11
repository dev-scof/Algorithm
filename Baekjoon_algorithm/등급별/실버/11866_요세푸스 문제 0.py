n, k = map(int, input().split())
arr = list(range(1, n+1))
result = []
i=0
k-=1
while arr:
    i = (i+k)%len(arr)
    result.append(arr.pop(i))
print('<'+', '.join(map(str, result))+'>')