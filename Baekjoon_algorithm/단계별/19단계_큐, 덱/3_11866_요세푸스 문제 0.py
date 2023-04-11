from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
rm_index=1
answer = []
queue = deque([x for x in range(1, N+1)])
while len(queue)!=0:
    if rm_index%K==0:
        answer.append(queue.popleft())
    else:
        queue.append(queue.popleft())
    rm_index+=1
print('<'+', '.join(map(str,answer))+'>')