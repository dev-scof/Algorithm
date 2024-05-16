# x보다 크고 x와 비트가 1~2개 다른 수들 중에서 제일 작은 수
#########################풀이1
'''
계속 +1하면서 비교 -> 시간 초과
'''
def f1(x):
    n = x
    while True:
        n += 1
        if bin(x ^ n).count('1') in (1, 2):
            return n
def solution1(numbers):
    answer = []
    for x in numbers:
        answer.append(f1(x))
    return answer
###############################
def solution2(numbers):
    # https://school.programmers.co.kr/questions/53534
    answer = []
    for x in numbers:
        n = x
        cnt = 0
        while n % 2:
            cnt += 1
            n //= 2
        if cnt:
            answer.append(x + 2**(cnt-1))
        else:
            answer.append(x+1)
    return answer
########################################
def solution(numbers):
    answer = []
    
    for x in numbers:
        bin_ = list('0' + bin(x)[2:])
        idx = ''.join(bin_).rfind('0')
        bin_[idx] = '1'
        if x % 2:
            bin_[idx+1] = '0'
        answer.append(int(''.join(bin_), 2))
    return answer

if __name__ == '__main__':
    print(solution([2, 7])) # [3,11]