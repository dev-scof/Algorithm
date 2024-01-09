graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1
from collections import deque

def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited
  
print(BFS_with_adj_list(graph_list, root_node))

def DFS_with_adj_list(graph, root):
    visited = [] # 방문한 리스트
    stack = [root] # 방문해야할 스택?

    while stack:
        print("*"*15)
        print("현재 스택 = ", stack)
        n = stack.pop() # 방문해야할 스택에서 가져옴
        print("현재 노드 = ", n)
        if n not in visited: # 가져온 값이 방문을 안한 경우
            visited.append(n) # 방문
            print("방문 한 노드 n = ", n)
            stack += graph[n] - set(visited) # 방문한 것을 지우고 스택에 삽입
            print("추가된 stack = ", graph[n] - set(visited))
    return visited

print(DFS_with_adj_list(graph_list, root_node))