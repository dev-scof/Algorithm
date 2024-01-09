def solution(s):
    S = list(s)
    S.sort(reverse=True)
    return ''.join(S)
print(solution("Zbcdefg"))