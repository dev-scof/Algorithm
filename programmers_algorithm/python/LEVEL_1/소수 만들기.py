def is_divisor(num):
    divisors = []
    divisors_back = []
    for i in range(1, int(num**(1/2))+1):
        if (num % i ==0):
            divisors.append(i)
            if (i != (num//i)):
                divisors_back.append(num//i)
    #print(divisors)
    #print(divisors_back)
    if len(divisors) == 1:
        return True

def solution(nums):
    cnt = 0
    _len = len(nums)
    for i in range(_len):
        for j in range(i+1, _len):
            for k in range(j+1, _len):
                # print("i = ", nums[i], "j = ", nums[j], "k = ", nums[k], "sum = ", nums[i]+nums[j]+nums[k])
                if is_divisor(nums[i]+nums[j]+nums[k]):
                    cnt+=1
    return cnt

print(solution([1,2,7,6,4]))

'''
약수의 개수에서 검색을 시도했다.
'임의의 자연수 N의 약수들 중에서 두 약수의 곱이 N이 되는 약수 A와 약수 B는 반드시 존재한다'
는 규칙이 존재하기 때문에, 자연수 N의 제곱근까지의 약수를 구하면 그 짝이 되는 약수는 자동으로 구해진다. (i, n//i)

'''