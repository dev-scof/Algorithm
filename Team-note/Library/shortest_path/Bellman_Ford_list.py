# https://velog.io/@younge/Python-%EC%B5%9C%EB%8B%A8-%EA%B2%BD%EB%A1%9C-%EB%B2%A8%EB%A7%8C-%ED%8F%AC%EB%93%9CBellman-Ford-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
# https://engkimbs.tistory.com/363
# 나동빈 유튜브 : https://www.youtube.com/watch?v=Ppimbaxm8d8
'''
모든 정점에 대해 최단 경로 테이블을 갱신하는 방법
음의 가중치를 갖는 그래프에서 최단 경로를 찾을 때 사용한다.

'''
import sys
input = sys.stdin.readline
INF = int(1e9)

def bellman_ford(start):
    # 시작 노드에 대해서 초기화
    dist[start] = 0
    
    # 전체 n번의 라운드를 반복
    for i in range(n):
        # 모든 간선을 확인, 반복
        for j in range(m):
            cur = edges[j][0]
            print('현재노드 = ', cur)
            next_node = edges[j][1]
            cost = edges[j][2]

            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 갱신
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                # n번째 라운드에서도 갱신이 일어난다면 음수 순환이 존재하는 것                
                if i == n-1:
                    return True
    return False

# 노드의 개수, 간선의 개수 입력
n, m = map(int, input().split())
# 모든 간선에 대한 정보를 담는 리스트 생성
edges = []
# 최단 거리 테이블을 모두 무한으로 초기화
dist = [INF] * (n+1)

# 모든 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a에서 b로 가는 비용이 c
    edges.append((a, b, c))

# 벨만 포드 알고리즘 수행
negative_cycle = bellman_ford(1) # 1번 노드부터 시작

if negative_cycle:
    # 음수 간선 순환 발생
    print('-1')
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
    for i in range(2, n+1):
        # 도달할 수 없는 경우 -1출력
        if dist[i] == INF:
            print('-1')
        else:
            print(dist[i])