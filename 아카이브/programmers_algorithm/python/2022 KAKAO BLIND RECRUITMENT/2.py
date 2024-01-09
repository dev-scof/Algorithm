def nProblem(n, dem):
    temp = []
    q, r = divmod(n, dem)
    temp.append(r)
    while q:
        q, r = divmod(q, dem)
        temp.append(r)
    return list(reversed(temp))
def is_prime(n):
    if n==1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def solution(n, k):
    answer = 0
    l = ''.join(map(str, nProblem(n, k))).split('0')# n진수
    for i in l:
        if i=='':
            continue
        if(is_prime(int(i))):
            answer+=1      
    return answer
print(solution(437674, 3))
print(solution(110011, 10))