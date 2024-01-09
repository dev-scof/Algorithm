def solution(price, money, count):
    answer = 0
    for i in range(1, count+1):
        answer+=price*i
    return 0 if money-answer>0 else answer-money
print(solution(3, 20, 4))
