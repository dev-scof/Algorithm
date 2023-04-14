from collections import deque
from copy import deepcopy
def bfs(v, visisted, graph):
    cnt = 0
    queue = deque([v])
    while queue:
        elem = queue.popleft()
        if elem not in visisted:
            cnt+=1
            visisted.add(elem)
            if elem not in graph:
                continue
            queue.extend(graph[elem])
    return cnt
            
def solution(n, wires):
    answer = 1e9
    graph = {}
    for u, v in wires:
        graph[u] = graph.get(u, [])+[v]
        graph[v] = graph.get(v, [])+[u]

    elements = set(graph.keys())
    for removed_edge in wires:
        # removed_edge = 삭제할 간선
        u, v = removed_edge
        visited = set()
        temp_graph = deepcopy(graph)
        temp_graph[u].remove(v)
        temp_graph[v].remove(u)
        # 임의의 정점에 대해 bfs를 수행
        cnt1 = bfs(list(graph.keys())[0], visited, temp_graph)
        # 방문하지 않은 정점 중 임의의 정점에 대해 bfs수행
        cnt2 = bfs(list(elements - visited)[0], visited, temp_graph)
        answer = min(answer, abs(cnt1-cnt2))
    
    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))