from itertools import permutations
prime_list = []


def is_prime(n: int):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    prime_list.append(n)
    return True


def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):
        answer += list(map(''.join, permutations(numbers, i)))
    answer = list(set(map(int, answer)))
    cnt = 0
    for n in answer:
        if n in prime_list or is_prime(n):
            cnt += 1
    return cnt

if __name__ == '__main__':
    print(solution("17"))  # 3
    print(solution("011"))  # 2
