'''
N개의 지점, N개의 지점 사이에는 M개의 도로와 W개의 웜홀이있다.
웜홀은 시작위치에서 도착위치로 가는 하나의 경로
특이하게도 도착을 하게 되면 시작했을때 보다 시간이 뒤로가게 된다.

한 지점에서 출발해서 다시 출발 위치로 돌아왔을때 출발했을때보다 시간이 
'''
import sys
input = sys.stdin.readline
TC = int(input())
INF = 1e9
def belman_ford(N, graph:dict):
    distance = [INF]*(N+1)
    # 처음 정점의 최단경로 0지정
    distance[1] = 0
    for check in range(N):
        for vertex, edges in graph.items():
            for next_vertex, dist in edges:
                cost = distance[vertex] + dist
                if distance[next_vertex] > cost:
                    distance[next_vertex]=cost
                    if check==N-1:
                        return True
    return False


for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = {}
    for __ in range(M):
        S, E, T = map(int, input().split())
        graph[S] = graph.get(S, [])
        graph[S].append((E, T))
        graph[E] = graph.get(E, [])
        graph[E].append((S, T))
        
    for __ in range(W):
        S, E, T = map(int, input().split())
        graph[S] = graph.get(S, [])
        graph[S].append((E, -T))

    if belman_ford(N, graph):
        print("YES")
    else:
        print("NO")