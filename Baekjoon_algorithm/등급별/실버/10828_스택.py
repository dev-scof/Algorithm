import sys
stack=[]
input = sys.stdin.readline
for _ in range(int(input())):
    string = input().rstrip().split()
    if len(string)==1:
        cmd=string[0]
        if cmd=='top':
            if stack==[]:
                print(-1)
            else:
                print(stack[-1])
        if cmd=='size':
            print(len(stack))
        if cmd=='empty':
            if stack==[]:
                print(1)
            else:
                print(0)
        if cmd=='pop':
            if stack==[]:
                print(-1)
            else:
                print(stack.pop())
    else:
        cmd, num = string
        if cmd=='push':
            stack.append(num)