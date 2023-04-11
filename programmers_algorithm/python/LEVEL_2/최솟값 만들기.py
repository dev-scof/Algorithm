def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    while A[:]:
        answer+= A[0]*B[0]
        A.pop(0)
        B.pop(0)    
    return answer

print(solution([1,4,2], [5,4,4]))