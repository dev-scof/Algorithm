# https://hooongs.tistory.com/177 참고
'''
이분 그래프의 개념

'''
from collections import deque
K = int(input())
def bfs(v):
    q = deque()
    q.append([v, 1]) # 정점 v을 그룹 1로 지정
    visited[v] = 1 # 정점 v 방문, 그룹은 1

    while q:
        v, g = q.popleft() # 현재 정점 v, 그룹 g
        if v not in graph:
            return False
        for e in graph[v]:
            if e not in visited:
                visited[e] = -g # 그룹 부호 반전
                q.append([e, -g])
def check():
    for v in graph.keys():
        for e in graph[v]:
            # 정점과 인접하는 정점과의 그룹이 다른지 체크
            # 같은 경우 -> 이분 그래프가 아님
            if visited[v] == visited[e]:
                return False
    return True
for _ in range(K):
    V, E = map(int, input().split())
    graph = {}
    visited={}
    for __ in range(E):
        u, v = map(int, input().split())
        # 양방향
        graph[u] = graph.get(u, [])
        graph[u].append(v)
        graph[v] = graph.get(v, [])
        graph[v].append(u)
    for i in graph.keys():
        if i not in visited: # 방문하지 않았다면
            visited[i] = 1
            bfs(i)
    if check():
        print('YES')
    else:
        print('NO')
