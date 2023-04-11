T = int(input())
l = []
for _ in range(T):
    l.append(int(input()))
stack=[]
answer=[]
flag=True
for i in range(1, T+1):
    stack.append(i) # 스택에 삽입
    answer.append('+')
    if stack[-1] >= l[0]: # 스택의 top의 값이 l[0]보다 클 경우 -> 스택에 l[0]의 값이 들어있음을 의미
        while stack != []:
            if stack[-1] < l[0]: # 스택의 top 값이 l[0]보다 작을 경우 -> 스택에 l[0]의 값이 들어있지 않음을 의미 
                # -> 새로운 값을 push해야하므로 break
                break
            if stack[-1] == l[0]: # 스택의 top 값과 l[0]와 같음 -> 스택 pop, l[0] pop
                stack.pop()
                l.pop(0)
            else: # 같지 않을 경우 -> 만들 수 없음을 의미 -> flag 설정
                flag=False
                break
            answer.append('-')
    if not flag:
        break
if flag:
    for a in answer:
        print(a)
else:
    print('NO')