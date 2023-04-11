from sys import stdin
input = stdin.readline
T = int(input())
stack = []
for _ in range(T):
    cmd = input().rstrip()
    if cmd=='top':
        if stack==[]:
            print(-1)
        else:
            print(stack[-1])
    elif cmd=='size':
        print(len(stack))
    elif cmd=='empty':
        if stack==[]:
            print(1)
        else:
            print(0)
    elif cmd=='pop':
        if stack==[]:
            print(-1)
        else:
            print(stack.pop())
    else: # push
        cmd, num = cmd.split()
        stack.append(int(num))