T = int(input())
for _ in range(T):
    str = input()
    stack=[]
    flag = True
    for s in str:
        if s=='(':
            stack.append('(')
        else:
            if stack==[]:
                flag=False
                break
            else:
                stack.pop()
    if flag and stack==[]:
        print("YES")
    else:
        print("NO")