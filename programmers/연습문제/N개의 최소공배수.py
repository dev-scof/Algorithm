def solution(arr):
    answer, divisor = 1, 2
    while divisor <= min(arr):
        for num in arr:
            if num % divisor == 1:
                divisor += 1
                break
        else:
            arr = list(map(lambda x:x//divisor, arr))
            answer *= divisor
    for num in arr:
        answer *= num
    return answer


def solution1(arr):
    answer, divisor = 1, 2
    while divisor <= (min(arr) ** 0.5) + 1:
        for num in arr:
            if num % divisor == 1:
                divisor += 1
                break
        else:
            arr = list(map(lambda x:x//divisor, arr))
            answer *= divisor
    for num in arr:
        answer *= num
    return answer



def solution2(arr):
    min_, answer = min(arr), 1
    for n in arr:
        answer *= n
    divisor = 1
    while divisor <= min_:
        if min_ % divisor == 0 and answer % divisor == 0:
            answer //= divisor**len(arr)
            answer *= divisor
        divisor += 1
    return answer

def solution3(arr):
    min_, answer = min(arr), 1
    divisor = 2
    while divisor <= min_:
        if min_ % divisor == 0:
            for num in arr:
                if num % divisor:
                    divisor += 1
                    break
            else:
                answer *= divisor
                arr = list(map(lambda x:x%divisor, arr))
        else:
            divisor += 1
    for num in arr:
        answer *= num
    return answer
'''
2 | 36, 48
2 | 18, 24
3 | 9, 12
    3, 4

2*2*3 => 최대 공약수
2*2*3*3*4 => 최소 공배수
'''

def solution4(arr):
    answer, divisor = 1, 2
    max_ = max(arr)
    while divisor <= max_:
        flag = False
        for n in arr:
            if n % divisor == 0:
                flag=True
                break
        if flag:
            answer *= divisor
            for i in range(len(arr)):
                if arr[i] % divisor == 0:
                    arr[i] = arr[i] // divisor
        else:
            divisor += 1
    return answer

if __name__ == "__main__":
    print(solution4([2,6,8,14]))
    # print(solution4([3,6,9,12]))
    # print(solution4([1,2,3]))
    # print(solution4([8, 12, 256]))
    # print(solution4([1,1,9,3,1]))