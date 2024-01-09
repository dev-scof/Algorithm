from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
rm_index = list(map(lambda x:x-1, list(map(int, input().split()))))

q = deque(range(N))
answer = 0
while rm_index != []:
    if q[0] == rm_index[0]:
        rm_index.pop(0)
        q.popleft()
    else:
        # q 회전시키기
        f_idx=q.index(rm_index[0]) # 찾으려는 인덱스 위치

        # 왼쪽으로 이동하는게 더 빠른 경우
        if f_idx < len(q)-f_idx:
            answer+=1
            q.append(q.popleft())
        
        # 오른쪽으로 이동하는게 더 빠른 경우
        else:
            answer+= 1
            q.appendleft(q.pop())
print(answer)