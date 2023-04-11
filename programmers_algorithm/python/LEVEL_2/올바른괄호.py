def solution(s):
    stack = []
    for i in s:
        if stack == [] and i == ')':
            return False # 잘못됨
        elif i == ')': # 스택에서 하나빼기
            stack.pop()
        else: # (가 들어오면, 어팬드
            stack.append('(')
    if stack==[]:
        return True
    else:
        return False
print(solution("(())"))
'''
test data
(())()
)
// ()
)
))
) // ()
//()

시간초과

def solution(s):
    stack = []
    print()
    if s[0] == ')' or s[len(s)-1] == '(' or list(s).count(')') != list(s).count('(') or list(s).count('(') > int(len(s)/2)+1 or list(s).count(')') > int(len(s)/2)+1:
        return False
    for i in s:
        if i == ')': # 닫혀있는 것이 들어오면
            if stack == []:
                return False
            else:
                stack.pop(0)
        else:
            stack.insert(0, i)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    if stack == []:
        return True
    else:
        return False
'''