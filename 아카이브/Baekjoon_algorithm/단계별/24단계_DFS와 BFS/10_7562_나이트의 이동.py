from collections import deque
TC = int(input())
dm = [
    (-2, -1), (-2, 1), 
    (-1, 2), (1, 2), 
    (2, 1), (2, -1), 
    (1, -2), (-1, -2)
    ] # 나이트 이동 경로

def bfs(cur, goal):
    q = deque()
    visited = set()
    flag = False
    depth = 0
    q.append(cur)
    visited.add(cur) # 현재 위치 방문
    while q:
        for _ in range(len(q)): # 큐에 담겨져있는 만큼 반복 -> 깊이 체크
            x, y = q.popleft() # 현재 위치, x, y
            if (x, y) == goal:
                flag=True
                break
            for dx, dy in dm: # 모든 방향에 대해 반복
                nx = x+dx # 이동한 x
                ny = y+dy # 이동한 y
                if nx<0 or ny<0 or nx>=l or ny>=l: # 벽을 넘어가면 패스
                    continue
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    q.append((nx, ny))
        if flag:
            break
        depth += 1
    return depth   

for _ in range(TC):
    l = int(input())
    x, y = map(int, input().split())
    cur = (x, y)
    x, y = map(int, input().split())
    goal = (x, y)
    print(bfs(cur, goal))
