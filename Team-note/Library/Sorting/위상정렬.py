from collections import deque

# 위상정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과 리스트
    q = deque()

    # 처음 시작할 때는 진입차수가 0인 노드를 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)

        # 키 에러 방지 코드
        if now not in graph:
            continue

        for i in graph[now]:
            # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    return result

if __name__ == '__main__':
    #노드의 개수와 간선의 개수 입력받기
    v, e = map(int, input().split())
    
    # 모든 노드에 대한 진입차수는 0으로 초기화
    indegree = [0] * (v + 1)

    # 각 노드에 연결된 간선 정보를 담기 위한 연결리스트 초기화
    graph = {}

    # 방향그래프의 모든 간선 정보 입력받기
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a] = graph.get(a, [])
        graph[a].append(b) # a -> b
        # b의 진입차수 1증가시키기
        indegree[b] +=1

    result = topology_sort()
    for i in result:
        print(i, end=' ')
        
'''
[Input Example 1]
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4

[Output Example 1]
1 2 5 3 6 4 7

'''