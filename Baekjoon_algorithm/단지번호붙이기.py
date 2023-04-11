import sys
input = sys.stdin.readline
N = int(input())
_map = []
for _ in range(N):
    _map.append(list(map(int, list(input().rstrip()))))

n_i = [0, 0, 1, -1]
n_j = [1, -1, 0, 0]

def dfs(c_i, c_j, visited):
    if c_i < 0 or c_j < 0 or c_i>=N or c_j>=N:
        return
    if _map[c_i][c_j] == 1:
        # 방문 처리
        visited.add((c_i, c_j))
        _map[c_i][c_j] = 0
        # 인접 노드 처리
        for d in range(4):
            d_i = c_i + n_i[d]
            d_j = c_j + n_j[d]
            dfs(d_i, d_j, visited)

cnt=0
answer = []
for i in range(N):
    for j in range(N):
        if _map[i][j]==1:
            visited = set()
            dfs(i, j, visited)
            cnt+=1
            answer.append(len(visited))
print(cnt)
answer.sort()
for a in answer:
    print(a)