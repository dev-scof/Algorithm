for _ in range(int(input())):
    word=input()
    stack=[]
    flag=True
    for w in word:
        if w == ')':
            if stack==[]:
                flag=False
                break
            else:
                stack.pop()
        elif w == '(':
            stack.append('(')
    if not flag or stack!=[]:
        print("NO")
    else:
        print("YES")
