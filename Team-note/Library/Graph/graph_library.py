from collections import deque

# Find the root node of x recursively.
# 루트노드 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# Union the two sets.
# a,b를 하나의 그룹으로 만들기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 무방향 그래프 내에서의 사이클 판별
# 간선정보, 부모정보를 받아 사이클이 있는지 체크하기
def undir_cycleCheck(edges, parent):
    '''
    # input - edges : 간선정보(리스트), parent : 부모정보 

    # output : 사이클 여부

    # 알고리즘
    각 간선을 하나씩 확인하며 두 노드(a, b)의 루트 노드를 확인합니다.
        - 루트 노드가 서로 다르다면 -> 두 노드에 대하여 합집합(Union)연산을 수행합니다.
        - 루트 노드가 서로 같다면 사이클이 발생한 것입니다.
    '''
    for a, b in edges:
        if find_parent(parent, a) == find_parent(parent, b):
            return True
        else:
            union_parent(parent, a, b)
    return False


# 방향 그래프 내에서의 사이클 판별
def dir_cycleCheck():
    pass


# 크루스칼 알고리즘
# 최소 신장 트리
# 간선정보와 부모정보를 받아 최소 비용을 출력
def Kruskal(Edges:list, parent:list):
    '''
    input - Edges : 간선정보, parent : 부모정보
    
    output - 최소 신장 트리의 최종 비용
    '''
    # 모든 간선을 비용 순으로 정렬
    Edges.sort()

    result = 0 # 최종 비용을 담을 변수

    # 모든 간선을 하나씩 확인
    for edge in Edges:
        cost, a, b = edge
        # 사이클이 발생하지 않는 경우에만 집합에 포함시키기
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
    
    return result




# 위상정렬 함수
# DAG
# 그래프와 진입차수(indegree)를 받아 정렬된 값 반환
def topology_sort(graph:dict, indegree:list):
    '''
    input - graph : 그래프(딕셔너리), indegree : 진입차수(리스트)

    output - 위상 정렬된 리스트
    
    '''
    result = [] # 알고리즘 수행 결과 리스트
    q = deque()

    # 처음 시작할 때는 진입차수가 0인 노드를 삽입
    for i in range(1, len(graph)+1):
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