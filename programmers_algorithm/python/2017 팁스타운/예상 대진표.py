from math import ceil
def solution(n,a,b):
    answer=0
    while ceil(a) != ceil(b):
        a/=2
        b/=2
        answer+=1
    return answer    
print(solution(8,4,7))