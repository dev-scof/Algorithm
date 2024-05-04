'''
def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibo(n-1)+fibo(n-2)

def solution(n):
    return fibo(n+1) % 1_000_000_007
'''
def solution2(n):
    dp = [0, 1, 2]
    for i in range(3, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n] % 1_000_000_007


def solution(n):
    num1, num2 = 1, 2
    for _ in range(n - 1):
        num1, num2 = num2, num1 + num2
    return num1 % 1_000_000_007

if __name__ == '__main__':
    print(solution(4))