from itertools import permutations
def is_prime(number):
    if number == 1 or number == 0:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i ==0:
            return False
    return True

def solution(numbers):
    answer = 0
    num_list = set()
    for i in range(1, len(numbers)+1):
        num_list |= set(map(int, map(''.join, permutations(numbers, i))))
    for num in num_list:
        if is_prime(num):
            answer+=1
    return answer

# print(solution("17"))
# print(solution("111111"))
print(solution("011"))