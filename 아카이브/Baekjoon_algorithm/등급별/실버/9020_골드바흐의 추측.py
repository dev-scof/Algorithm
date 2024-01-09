def is_prime(num):
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def sol(num):
    for n in range(int(num/2), num+1):
        if is_prime(n):
            if is_prime(num-n):
                print(num-n, n)
                return
for _ in range(int(input())):
    n = int(input())
    sol(n)