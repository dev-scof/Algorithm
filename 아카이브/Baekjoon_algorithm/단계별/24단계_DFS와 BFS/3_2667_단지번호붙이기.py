N = int(input()) # 지도의 크기
Map = []
for _ in range(N):
    Map.append(list(map(int, input())))

def dfs(x, y, visited):
    # 지도를 벗어날 경우 -> return
    if x<=-1 or x>=N or y<=-1 or y>=N:
        return False
    
    if Map[x][y]==1: # 방문하지 않음
        visited.add((x,y)) # 방문한 좌표 visited에 추가
        Map[x][y]=0
        #상, 하, 좌, 우의 dfs호출
        dfs(x-1, y, visited)
        dfs(x,y-1, visited)
        dfs(x+1,y, visited)
        dfs(x,y+1, visited)
        return True
    return False

answer = [] # 집의 수를 오름차순으로 만들기 위한 리스트
cnt = 0 # 단지수를 저장할 변수
for i in range(N):
    for j in range(N):
        # 집이 있을 경우
        if Map[i][j]==1:
            # 방문을 초기화 -> 집의 수를 알기 위해서
            visited=set()
            # dfs 실행
            dfs(i, j, visited)
            # len(visited) : 연결된 집의 수
            answer.append(len(visited))
            cnt+=1
answer.sort()
print(cnt)
for a in answer:
    print(a)