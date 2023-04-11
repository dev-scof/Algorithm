def solution(n):
    answer = 0
    start_num = 1
    while start_num <=n:
        _sum = 0
        temp = start_num
        while _sum<=n:
            _sum+=start_num
            start_num+=1
            if _sum == n:
                answer+=1
                break
        
        start_num = temp+1

    return answer
print(solution(15))