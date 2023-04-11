def solution(s):
    answer = 0
    stack = []
    for c in s:
        if stack == []:
            stack.append(c)
        elif stack[-1] == c: #같은경우
            stack.pop()
        else: #다른경우
            stack.append(c)
    if stack == []:
        return 1
    else:
        return 0
print(solution('cdcd'))