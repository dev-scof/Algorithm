# 메모리 초과 이슈가 있었다.
# 1. set을 사용해서 메모리 초과로 틀렸다고 생각하여 리스트로 바꾸었으나 시간초과가 발생했다.
# 2. x*2가 K*2일 경우, 거리가 범위를 넘어섰다고 생각되기에 경로에서 제외를 했더니
# 통과되었다.
from collections import deque
N, K = map(int, input().split())
q = deque()
q.append(N) # 현재 위치 저장
visited = set()
visited.add(N)
depth = 0
flag=False
while q:
    for _ in range(len(q)):
        x = q.popleft() # 현 위치
        if x ==K:
            flag=True
            break
        # x*2로 이동할 경우
        if x*2 not in visited:
            visited.add(x*2)
            if x*2<K*2: # 메모리 초과를 막기위한 임시코드.
                q.append(x*2)
        # x-1로 이동할 경우
        if x-1 not in visited:
            visited.add(x-1)
            q.append(x-1)
        # x+1로 이동할 경우
        if x+1 not in visited:
            visited.add(x+1)
            q.append(x+1)
    if flag:
        break
    depth+=1
print(depth)