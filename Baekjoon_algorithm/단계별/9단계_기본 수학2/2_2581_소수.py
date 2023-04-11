def is_prime(n):
    if n==1:
        return False
    for i in range(2, int(n**0.5)+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False
    return True
M = int(input())
N = int(input())
answer= min = 0
for i in range(M, N+1):
    if is_prime(i):
        if answer==0:
            min=i
        answer+=i
if answer==0:
    print(-1)
else:
    print(answer)
    print(min)