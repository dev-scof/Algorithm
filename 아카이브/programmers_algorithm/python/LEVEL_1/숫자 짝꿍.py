from collections import Counter
def solution(X, Y):
    answer=''
    X = Counter(X)
    Y = Counter(Y)
    for x in sorted(X.keys(), reverse=True):
        if x in Y:
            if answer=='' and x=='0':
                answer += '0'
            else:
                answer += x*min(X[x], Y[x])
    if answer=='':
        return '-1'
    return str(answer)


print(solution("100", "2345"))
print()
print(solution("100", "203045"))
print()
print(solution("100", "123450"))
print()
print(solution("12321", "42531"))
print()
print(solution("5525", "1255"))