from collections import deque
n, k = map(int, input().split())
q = deque()
q.append(n)
cnt=0
visited=set()
flag=False
while q:
    for _ in range(len(q)):
        x = q.popleft()
        if x<0 or x>100_000:
            continue
        visited.add(x)
        if x==k:
            flag=True
            break
        if x*2 not in visited:
            q.append(x*2)
        if x+1 not in visited:
            q.append(x+1)
        if x-1 not in visited:
            q.append(x-1)
    if flag:
        break
    cnt+=1
print(cnt)