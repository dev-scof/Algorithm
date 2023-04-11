N = int(input())
prime_list = [True]*(1234567) 
for i in range(2, int(1234567**0.5)+1): 
    if prime_list[i] == True:
        for j in range(i+i, 1234567, i):
            prime_list[j]=False
while N:
    if N == 1:
        print(N)
    else:
        cnt=0
        for i in range(N+1, N*2):
            if prime_list[i]:
                cnt+=1
        print(cnt)
    N = int(input())