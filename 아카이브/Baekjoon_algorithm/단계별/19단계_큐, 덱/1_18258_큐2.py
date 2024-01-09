# import sys
# input = sys.stdin.readline
# 추가를 안하여 시간초과
from collections import deque
import sys
q = deque()
def queue_api(line):
    command = line[0]

    if command == 'pop': # 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if q:
            return q.popleft()
        else:
            return -1
    elif command == 'size': # 큐에 들어있는 정수의 개수를 출력한다.
        return len(q)

    elif command == 'empty': # 큐가 비어있으면 1, 아니면 0을 출력한다.
        if q:
            return 0
        else:
            return 1
    elif command == 'front': # 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if q:
            return q[0]
        else:
            return -1
    elif command == 'back': # 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if q:
            return q[-1]
        else:
            return -1

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    line = list(input().split())
    # push 만 따로 처리
    if line[0] == 'push': # 정수 X를 큐에 넣는 연산이다.
        num = line[1]
        q.append(num)
    else:
        print(queue_api(line))