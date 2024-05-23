from itertools import permutations

'''
def solution1(numbers):
    # 시간 초과
    answer = permutations(numbers)

    result = []
    for i in answer:
        result.append(int(''.join(map(str, list(i)))))

    return str(max(result))
'''


def solution(numbers):
    if sum(numbers) == 0:
        return '0'
    numbers = list(map(str, numbers))
    numbers.sort(
        key=lambda x: x*3,  # numbers의 원소는 1000이하 -> 3자리수로 맞추기
        reverse=True
    )
    answer = ''.join(map(str, numbers))
    return answer if int(answer) else '0'


if __name__ == '__main__':
    print(solution([6, 10, 2])) # "6210"
    print(solution([3, 30, 34, 5, 9])) # "9534330"
    print(solution([0, 0, 0, 0, 0])) # "0"