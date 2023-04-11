def divisor_cus(N):
    divisors = []
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            divisors.append(i)
    return divisors
N = int(input())
divs=divisor_cus(N) # 2부터 시작
i=0
while i<len(divs):
    if N%divs[i] == 0:
        print(divs[i])
        N//=divs[i]
        continue
    else:
        i+=1
if N>1:
    print(N)
'''
n = int(input())
i = 2

while i <= int(n ** 0.5):
    while not n % i:
        print(i)
        n //= i
    i += 1
if n > 1:
    print(n)

'''