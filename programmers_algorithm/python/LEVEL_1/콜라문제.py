def solution(a, b, n):
    answer = 0
    while n>=a:
        add = (n//a)*b
        n = n%a+add
        answer+=add
    return answer

print(solution(2, 1, 20))
print(solution(3, 1, 20))