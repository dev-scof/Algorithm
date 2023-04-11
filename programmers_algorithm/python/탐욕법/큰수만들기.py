def solution(number, k):
    answer = ''
    stack = [number[0]]
    for i in number[1:]:
        while stack != [] and stack[-1] < i and k > 0:
            k-=1
            stack.pop()
        stack.append(i)
    
    
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)

#print(solution("4177252841",4))
print(solution("9999991",4))

'''
4177252841
stack = [4]

i = 1
stack[-1] > i이므로 반복문안돌음
stack.append(i) -> stack = [4,1]

i = 7
stack[-1] <i이므로 반복문 진입
stack.pop() -> stack = [4]
stack[-1] <i이므로 반복
stack.pop() -> stack = []
stack.append(i) -> stack = [7]

i = 7
stack[-1] > i이므로 반복문 안돌음
stack.append(i) -> stack = [7,7]


'''