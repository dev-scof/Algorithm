import sys
sys.setrecursionlimit(100000) # recursion limit 설정

def dfs1(cur):
    visited[cur] = True
    for nxt in adj_list[cur]:
        if not visited[nxt]:
            dfs1(nxt)
    stack.append(cur)

def dfs2(cur, cnt):
    visited[cur] = True
    scc[cur] = cnt
    for nxt in rev_adj_list[cur]:
        if not visited[nxt]:
            dfs2(nxt, cnt)

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    adj_list = [[] for _ in range(N+1)]
    rev_adj_list = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        adj_list[x].append(y)
        rev_adj_list[y].append(x)

    visited = [False] * (N+1)
    stack = []
    for i in range(1, N+1):
        if not visited[i]:
            dfs1(i)

    visited = [False] * (N+1)
    scc = [0] * (N+1)
    cnt = 0
    while stack:
        cur = stack.pop()
        if not visited[cur]:
            dfs2(cur, cnt)
            cnt += 1

    # SCC 간의 간선 개수 찾기
    in_degree = [0] * cnt
    for i in range(1, N+1):
        for j in adj_list[i]:
            if scc[i] != scc[j]:
                in_degree[scc[j]] += 1

    ans = 0
    for i in range(cnt):
        if in_degree[i] == 0:
            ans += 1

    print(ans)
