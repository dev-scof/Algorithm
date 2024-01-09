from collections import deque
def bfs():
    pass

n = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]

for _ in range(int(input())):
    l=int(input())
    cur_pos = tuple(map(int, input().split()))
    fin_pos = tuple(map(int, input().split()))
    q = deque()
    q.append(cur_pos)
    # bfs
    depth=0
    flag=False
    visited=set()
    while q:
        for _ in range(len(q)):
            c_pos = q.popleft()
            if c_pos==fin_pos:
                flag=True
                break
            for n_pos in n:
                d_pos = (c_pos[0]+n_pos[0], c_pos[1]+n_pos[1])
                if d_pos[0]<0 or d_pos[0]>=l or d_pos[1]<0 or d_pos[1]>=l:
                    continue
                if d_pos not in visited:
                    q.append(d_pos)
                    visited.add(d_pos)
        if flag:
            break
        depth+=1
    print(depth)