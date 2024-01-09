''' 시행착오
1. key Error
    #입력 값
    5 1 2
    3 4
    -> 시작점에 연결된 간선이 하나도 없을 경우
'''
from collections import deque
N, M, S = map(int, input().split())
graph={}
visited_dfs=set() # 들어있으면 방문한 것, dfs를 위한 집합

# 그래프 입력, 양방향
for _ in range(M):
    a, b = map(int, input().split())
    graph[a] = graph.get(a, []) + [b] # a->b
    graph[b] = graph.get(b, []) + [a] # b->a

for i in graph: 
    # 문제에서 방문할 수 있는 정점이 여러개의 경우, 
    # 작은 것부터 방문한다고 하였으므로 
    # 연결되어있는 정점에 대해 오름차순으로 정렬
    graph[i].sort()

def dfs(v):
    visited_dfs.add(v) # 정점 방문처리
    print(v, end=' ') # 방문한 정점 출력
    
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    if v not in graph: # key error을 반영한 코드, 시작점이 그래프에 없을 경우 -> 끝냄 
        return
    # 방문하지 않은 정점이 연결되어있을 경우,
    # 그 노드에 대해 다시 탐색
    for i in graph[v]:
        if i not in visited_dfs:
            dfs(i)

# def dfs(v):
#     stack=[v]
#     visited = set()
#     for i in graph: 
#         graph[i].sort(reverse=True)
#     while stack:
#         cur_node = stack.pop()
#         if cur_node not in visited:
#             print(cur_node, end=' ')
#             visited.add(cur_node)
#             if cur_node in graph:
#                 stack.extend(graph[cur_node])


def bfs(v):
    q = deque()
    visited_bfs=set() # 방문 집합 초기화
    q.append(v) # 큐에 넣고 시작
    for i in graph: 
        graph[i].sort()
    while q:
        # 큐에서 하나를 꺼내고
        n = q.popleft()
        # 방문하지 않았다면
        if n not in visited_bfs:
            # visited에 추가하고
            visited_bfs.add(n)
            print(n, end=' ')
            if n not in graph: 
                # key error을 반영한 코드, 
                # 시작점이 그래프에 없을 경우 -> 끝냄
                break
            # 방문하지 않은 정점(n)에 연결된 간선의 정보를
            # q에 담는다.
            q.extend(graph[n])
dfs(S)
print()
bfs(S)