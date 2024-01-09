def get_parent(parent, a):
    if parent[a] < 0:
        # 음수이면 -> 바로 a 반환, a는 양수임
        return a
    if parent[a] != a:
        parent[a] = get_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    # 같은 집합이면 -> pass
    if a==b:
        return
    parent[a] += parent[b]
    parent[b] = a # b의 parent를 a로 설정

def solution(n, wires):
    answer = int(1e9)
    k = len(wires) # k : 간선의 개수
    for i in range(k):
        parent = [-1 for _ in range(n+1)] # uf 초기화
        removed_edges = [wires[x] for x in range(k) if x != i] # 하나의 간선을 제외한 나머지 간선만 남겨둠
        
        # 하나의 간선이 제거된 간선에 대해 연결을 수행한다.
        for a, b in removed_edges:
            union_parent(parent, a, b)
            # print(f'parent 갱신 = {parent}')
        v = [x for x in parent[1:] if x < 0]
        # print(v)
        # print(parent)
        answer = min(answer, abs(v[0]-v[1]))
    return answer


print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
# print(solution(4, [[1,2],[2,3],[3,4]]))
# print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))