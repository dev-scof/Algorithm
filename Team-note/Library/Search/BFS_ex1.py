from collections import deque
N, M, S = map(int, input().split())
graph={}

def bfs(start, graph):
    visited=set() # 들어있으면 방문한 것

    # 큐 구현을 위해 deque 사용
    queue = deque()
    ############ 시작노드 처리  #############
    # 방문처리
    visited.add(start)
    # 큐에 삽입
    queue.append(start)
    ########################################
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된 인접 노드들에 대해 반복
        for i in graph[v]:
            if i not in visited:
                # 큐에 삽입하고
                queue.append(i)
                # 방문처리
                visited.add(i)

# 그래프 입력, 양방향
for _ in range(M):
    a, b = map(int, input().split())
    graph[a] = graph.get(a, []) + [b] # a->b
    graph[b] = graph.get(b, []) + [a] # b->a


bfs(S, graph)
'''
[Input Example 1]
4 5 1
1 2
1 3
1 4 
2 4
3 4

[Output Example 1]
1 2 3 4
'''