import sys
import os
sys.path.append(os.environ['Team_Note_Path'])

'''
input : 간선의 정보(cost, a, b)와 부모의 정부(parent)를 받아
output : 최소 신장트리의 최종 비용을 출력
'''
# 서로소 집합 메소드
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# Union the two sets.
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def Kruskal(Edges:list, parent:list):
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

if __name__ == '__main__':
    # 노드의 개수와 간선의 개수 입력받기
    v, e = map(int, input().split())

    edges = [] # 간선을 담을 리스트

    # 부모 테이블 초기화
    parent = [0] * (v+1)
    for i in range(1, v+1):
        parent[i] = i
    
    # 모든 간선에 대한 정보 입력받기
    for _ in range(e):
        a, b, cost = map(int, input().split())
        # 비용순으로 정렬하기 위해 cost를 첫번째 원소로 설정
        edges.append((cost, a, b)) # a -> b로가는 비용 cost
    
    # 크루스칼 알고리즘 수행
    result = Kruskal(edges, parent)
    print(result)

'''
[Input Example 1]
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25

[Output Example 1]
159

'''