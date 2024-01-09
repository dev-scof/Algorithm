def is_correct(s):
    stack = []
    for i in s:
        if stack == []: # 스택이 비어있으면
            stack.append(i)
        elif stack[-1] == '(' and i == ')':
            stack.pop()
        elif stack[-1] == '{' and i == '}':
            stack.pop()
        elif stack[-1] == '[' and i == ']':
            stack.pop()
        else:
            stack.append(i)
    if stack == []:
        return True
    else:
        return False        
def solution(s):
    correct = set()
    s = list(s)
    answer = 0
    for i in range(len(s)):
        if str(s) in correct: # 올바르게 있으면
            answer+=1
        elif is_correct(s): # 올바른 괄호라면
            correct.add(''.join(s))
            answer+=1
        s.append(s.pop(0))
    return answer
print(solution("[](){}"))