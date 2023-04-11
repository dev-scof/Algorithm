'''
간선정보(edges)와 부모정보(parent)를 넘겨주어 판별한다.
'''
from graph_library import *
# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화
graph = {} # 그래프
edges = []
# 부모 테이블상에서, 각각의 부모를 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 사이클 여부
cycle = False

# 그래프 입력받기
for i in range(e):
    a, b = map(int, input().split())
    
    # 간선 정보 담기
    edges.append((a, b))

    # 무방향 그래프
    graph[a] = graph.get(a, [])
    graph[a].append(b)
    graph[b] = graph.get(b, [])
    graph[b].append(a)


if undir_cycleCheck(edges, parent):
    print('사이클이 발생했습니다.')
else:
    print('사이클이 발생하지 않았습니다.')
'''
[input1]
3 3
1 2
1 3
2 3


[output1]
사이클이 발생했습니다.
*****************************
[input2]
4 3
1 2
1 3
2 4

[output2]
사이클이 발생하지 않았습니다.


'''