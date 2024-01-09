from collections import deque
import sys
input = sys.stdin.readline
queue = deque()
T = int(input())
for _ in range(T):
    command = input().split()
    if command[0] == 'push_front':
        queue.appendleft(int(command[1]))

    if command[0] == 'push_back' :
        queue.append(int(command[1]))

    if command[0] == 'pop_front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue.popleft())
    if command[0] == 'pop_back':
        if len(queue)==0:
            print(-1)
        else:
            print(queue.pop())
    if command[0] == 'size':
        print(len(queue))

    if command[0] == 'empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)
    if command[0] == 'front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
            
    if command[0] == 'back':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])
