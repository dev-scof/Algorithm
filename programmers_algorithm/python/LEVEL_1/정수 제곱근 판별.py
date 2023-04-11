def solution(n):
    result = pow(n, 0.5)
    return pow(int(result)+1, 2) if result.is_integer() else -1

print(solution(121))