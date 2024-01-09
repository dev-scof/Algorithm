def solution(n):
    answer = 0
    for i in range(1, n//2+1):
        if n%i==0:
            answer+=i
    return answer
print(solution(12))
'''
num / 2까지만 돌리면 성능이 2배정도 증가한다.
def sumDivisor(num):
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

    1~n//2까지의 range에서 num %i ==0이 되는 값만 리스트로 만들고
    그것의 sum연산을 하고 
    num을 더한다.
'''