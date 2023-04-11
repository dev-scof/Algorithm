while True:
    n = int(input())
    if n==-1:
        break
    divisor=[]
    for i in range(1, n+1):
        if n%i==0:
            divisor.append(i)
    if n==sum(divisor[:-1]):
        print(f'{n} = '+' + '.join(map(str, divisor[:-1])))
    else:
        print(f'{n} is NOT perfect.')