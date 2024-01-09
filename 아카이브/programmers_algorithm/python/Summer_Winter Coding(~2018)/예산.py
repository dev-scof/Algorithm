def solution(d, budget):
    answer = 0
    for i in d[:]:
        Min = min(d)
        budget -= Min
        if budget>=0:
            answer+=1
            d.remove(Min)
        else:
            break
    return answer
print(solution([2,2,3,3], 10))