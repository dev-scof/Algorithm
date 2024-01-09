def isRight(s): # 올바른 괄호면 , 아니면 0
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
def split_String(s):
    open_cnt = 0
    close_cnt = 0
    if s =="":
        return '', ''
    if s[0] == '(':
        open_cnt+=1
    else:
        close_cnt+=1
    
    for i in range(1, len(s)):
        if open_cnt == close_cnt:
            u = s[0:i]
            v = s[i:]
            return u, v
        if s[i] == '(':
            open_cnt+=1
        else:
            close_cnt+=1
    return s, '' # 완전한 문자열
def Recursive_String(s):
    if s == '':
        return ''
    u, v = split_String(s)
    if isRight(u): # u가 올바른 괄호면
        return u + Recursive_String(v)        
    else: # u가 올바른 문자열이 아니다.
        print("올바르지 않은 u = ", u)
        new_string = '('
        new_string += Recursive_String(v)
        new_string+=')'
        for i in u[1:-1]:
            if i ==')':
                new_string += '('
            else:
                new_string += ')'
        return new_string


def solution(p):
    if p == '' : # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
        return ''
    answer = Recursive_String(p)   
    return answer
print(solution("(()())()"))
