import sys

def bfs(x):
    visited = [-1] * (N+1)
    visited[x] = 0
    q = [x]
    while q:
        now = q.pop()
        for i, cost in tree[now]:
            if visited[i] == -1:
                visited[i] = visited[now] + cost
                q.append(i)
    return visited

def main():
    global tree, N
    I = sys.stdin.readline
    N = int(I())
    tree = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b, c = map(int,I().split())
        tree[a].append((b, c))
        tree[b].append((a, c))
    res1 = bfs(1)
    idx = res1.index(max(res1))
    print(max(bfs(idx)))

if __name__ == "__main__":
    main()