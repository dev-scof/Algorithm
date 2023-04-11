def divisor(num):
    divisors = []
    divisors_back = []
    for i in range(1, int(num**(1/2))+1):
        if (num % i ==0):
            divisors.append(i)
            if (i != (num//i)):
                divisors_back.append(num//i)
    return len(divisors+divisors_back)
def solution(left, right):
    answer=0
    for i in range(left, right+1):
        if divisor(i)%2==0: #짝수
            answer+=i
        else:
            answer-=i
    return answer
print(solution(13, 17))

