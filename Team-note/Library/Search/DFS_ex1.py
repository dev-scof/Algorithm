from collections import defaultdict
N, M, S = map(int, input().split())
graph={}
visited_dfs=set() # 들어있으면 방문한 것, dfs를 위한 집합

# 그래프 입력, 양방향
for _ in range(M):
    a, b = map(int, input().split())
    graph[a] = graph.get(a, []) + [b] # a->b
    graph[b] = graph.get(b, []) + [a] # b->a

def dfs(v):
    visited_dfs.add(v) # 정점 방문처리
    print(v, end=' ') # 방문한 정점 출력
    
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    if v not in graph: # key error을 반영한 코드, 시작점이 그래프에 없을 경우 -> 끝냄 
        return

    for i in graph[v]:
        # 연결된 정점에 대해 반복하는데,
        # 방문하지 않은 노드일 경우 -> dfs 다시 수행
        if i not in visited_dfs:
            dfs(i)

def dfs_stack(S):
    stack_dfs = []
    visited = set()
    stack_dfs.append(S) # 시작노드 S로 설정

    # 숫자가 작은 순서대로 꺼내기 위해 인접노드를 내림차순으로 정렬
    for v in graph.keys():
        graph[v].sort(reverse=True)


    # 스택이 빌때까지 반복
    while stack_dfs:
        # 최상위 노드를 꺼냄
        node = stack_dfs.pop()

        # node가 방문하지 않았다면
        if node not in visited:
            # 방문처리
            visited.add(node)
            print(node, end=' ')
            # 인접노드 스택에 추가하기
            stack_dfs.extend(graph[node])

dfs_stack(S)
'''
[Input Example 1]
4 5 1
1 2
1 3
1 4 
2 4
3 4

[Output Example 1]
1 2 4 3
'''