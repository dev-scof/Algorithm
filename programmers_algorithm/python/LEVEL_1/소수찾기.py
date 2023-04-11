def solution(n):
    answer = 0
    '''
    for i in range(2, n+1):
        flag=True
        for j in range(2, (i//2)+1):
            if i%j==0:
                flag = False
                break
        if flag:
            answer+=1
    return answer
    '''
    prime_list = [True]*(n+1) 
    
    for i in range(2, int(n**0.5)+1): 
        if prime_list[i] == True:
            for j in range(i+i, n+1, i):
                prime_list[j]=False 
    print(prime_list)
    return (len([i for i in range(2, n+1) if prime_list[i]==True]))
print(solution(5))