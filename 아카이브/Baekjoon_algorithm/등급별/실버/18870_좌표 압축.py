n = int(input())
arr = list(map(int, input().split()))
ranks = dict( map(lambda x:(x[1],x[0]), enumerate(sorted(set(arr)))) )
for num in arr:
    print(ranks[num], end=' ')