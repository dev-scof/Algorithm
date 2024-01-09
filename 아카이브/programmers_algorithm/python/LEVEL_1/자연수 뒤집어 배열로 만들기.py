def solution(n):
    return list(map(int, list(reversed(str(n)))))
    
    
print(solution(12345))