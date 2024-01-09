from collections import deque
for _ in range(int(input())):
    n, m = map(int, input().split())
    # n: 현재 문서의 개수
    # m: 궁금한 문서가 현재 큐에서 몇번째 놓여있는지
    prior = deque(enumerate(map(int, input().split())))
    cnt=0
    while True:
        cur = prior.popleft()
        flag=True
        for i, v in prior:
            if cur[1]<v:
                prior.append(cur)
                flag=False
                break
        if flag:
            if cur[0]==m:
                print(cnt+1)
                break
            else:
                cnt+=1