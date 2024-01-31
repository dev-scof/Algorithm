def is_right(s):
    stack = []
    for w in s:
        if w == '(' or w == '{' or w == '[':
            stack.append(w)
        elif not stack:
            return False
        elif (
            stack[-1] == '(' and w == ')'
            or stack[-1] == '{' and w == '}'
            or stack[-1] == '[' and w == ']'
        ):
            stack.pop()
    if stack:
        return False
    return True

def solution(s):
    answer, length = 0, len(s)
    s += s
    for i in range(length):
        if is_right(s[i:i+length]):
            answer += 1
    return answer

if __name__ == '__main__':
    print(solution("[](){}"))
    print(solution("}]()[{"))
    print(solution("[)(]"))
    print(solution("}}}"))
