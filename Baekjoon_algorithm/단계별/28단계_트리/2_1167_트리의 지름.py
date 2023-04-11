'''
https://ca.ramel.be/112
'''
import sys
input = sys.stdin.readline

from collections import defaultdict
V = int(input())
graph = defaultdict(list)
for _ in range(V):
    line = list(map(int, input().split()))
    u = line[0]
    line.pop(0)
    for i in range(len(line)//2):
        v, w = line[i*2], line[i*2+1]
        # print(u, v, w)
        if (v, w) not in graph[u]:
            graph[u].append((v, w))
        if (u, w) not in graph[v]:
            graph[v].append((u, w))

def distance(s, result):
    for e, d in graph[s]:
        if result[e] == 0:
            result[e] = result[s] + d
            distance(e, result)
result1 = [0 for _ in range(V+1)]
distance(1, result1)
result1[1] = 0

tmpMax = 0
tmpIdx = 0
for i, x in enumerate(result1):
    if tmpMax < x:
        tmpMax = x
        tmpIdx = i

result2 = [0 for _ in range(V+1)]
distance(tmpIdx, result2)
result2[tmpIdx] = 0
print(max(result2))


'''
5
1 3 2 -1
2 4 4 -1
3 1 2 4 3 -1
4 2 4 3 3 5 6 -1
5 4 6 -1


5
1 3 2 -1
2 4 11 -1
3 1 2 4 3 -1
4 2 11 3 3 5 6 -1
5 4 6 -1
'''