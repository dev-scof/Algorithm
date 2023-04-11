# 방법 1. math 라이브러리 사용
import math
num = int(input())


# 방법 2. 단순 반복
def factorial(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret

# 방법 3. 재귀
def factorial_recur(n):
    if n==1:
        return n
    return n*factorial_recur(n-1)

print(math.factorial(num))
print(factorial(num))
print(factorial_recur(num))

# 방법 4. 재귀+DP
