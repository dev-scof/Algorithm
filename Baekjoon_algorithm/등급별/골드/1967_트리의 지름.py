import sys
sys.setrecursionlimit(100000)
N = int(input())
tree=dict()
for _ in range(N-1):
    parent, child, weight = map(int, input().split())
    tree[parent] = tree.get(parent, [])
    tree[parent].append([child, weight])

def dfs(node, cost, result):
    if node not in tree:
        result.append(cost)
        return result
    for n in tree[node]:
        dfs(n[0], cost+n[1], result)
    return result


answer = 0
for key in tree:
    length = []
    for node in tree[key]:
        res = dfs(node[0], node[1], [])
        length.append(max(res))
    length.sort(reverse=True)
    if len(length)>=2:
        answer = max(answer, length[0]+length[1])
    elif len(length)==1:
        answer = max(answer, length[0])
print(answer)