from collections import deque


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    number = deque()
    while n:
        n, r = divmod(n, k)
        if r == 0:
            number = ''.join(map(str, number)) if number else None
            if number and is_prime(int(number)):
                answer += 1
            number = deque()
        else:
            number.appendleft(r)
    number = ''.join(map(str, number)) if number else None
    if number and is_prime(int(number)):
        answer += 1
    return answer


if __name__ == '__main__':
    # print(is_prime(11))
    print(solution(437674, 3))
    print(solution(110011, 10))