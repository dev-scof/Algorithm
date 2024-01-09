def solution(a, b):
    answer = 0
    Mx = max(a,b)
    Mn = min(a,b)
    for i in range(Mn, Mx+1):
        answer += i
    return answer

print(solution(3,5))