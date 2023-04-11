def solution(n):
    fibo = [0,1,1]
    if n==2:
        return 1
    for i in range(1, n):
        fibo.append(fibo[i]+fibo[i+1])
    
    return fibo[n]%1234567
print(solution(3))