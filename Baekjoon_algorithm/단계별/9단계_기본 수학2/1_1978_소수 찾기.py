def is_prime(n):
    if n==1:
        return False
    for i in range(2, int(n**0.5)+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False
    return True
if __name__ == '__main__':
    T = int(input())
    nums = list(map(int, input().split()))
    answer = 0
    for i in nums:
        if is_prime(i):
            answer+=1
    print(answer)
