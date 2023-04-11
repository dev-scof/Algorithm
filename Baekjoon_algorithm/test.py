class Graph:
    def __init__(self) -> None:
        self.graph = {}
        self.visited = set()
        self.write = []
    
    # 간선 생성
    def add_edge(self, u, v):
        self.graph[u] = self.graph.get(u, [])+[v]
        self.graph[v] = self.graph.get(v, [])+[u]

    ###########################
    # dfs 탐색, v정점부터 시작 #
    ###########################
    def search_dfs(self, v):
        # 정점에 연결된 간선에 대해 정렬
        for i in self.graph:
            self.graph[i].sort()
        
        # visited 초기화
        self.visited = set()
        self.write = []
        return self.recur_dfs(v)
    
    def recur_dfs(self, v):
        # 방문
        self.write.append(v)
        self.visited.add(v) # 정점 방문처리
        
        # 입력된 노드가 그래프에 없으면 수행하지않음
        if v not in self.graph:
            return
        
        # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        for edge in self.graph[v]:
            if edge not in self.visited:
                self.recur_dfs(edge)


graph = Graph()
N = int(input())
for _ in range(N):
    u, v = map(int, input().split())
    graph.add_edge(u, v)
graph.search_dfs(1)
print(graph.write)
