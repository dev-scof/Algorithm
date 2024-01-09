def solution(prices):
    answer = []
    for i, value in enumerate(prices):
        result = 0
        for j in range(i+1, len(prices)):
            result +=1
            if value > prices[j]:
                break
        answer.append(result)
    return answer
print(solution([1, 2, 3, 2, 3]))