while True:
    str = input()
    if str=='.':
        break
    stack=[]
    flag = True
    for s in str:
        if s=='(':
            stack.append('(')
        elif s=='[':
            stack.append('[')
        elif s==')':
            if stack==[] or stack[-1] != '(':
                flag=False
                break
            else:
                stack.pop()
        elif s==']':
            if stack==[] or stack[-1] != '[':
                flag=False
                break
            else:
                stack.pop()
    if flag and stack==[]:
        print("yes")
    else:
        print("no")