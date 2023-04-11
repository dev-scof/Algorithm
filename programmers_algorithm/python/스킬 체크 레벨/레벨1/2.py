def solution(n):
    temp = []
    answer = 0
    q, r = divmod(n, 3)
    temp.append(r)
    while q:
        q, r = divmod(q, 3)
        temp.append(r)
    n=0
    while temp != []:
        answer += (3**n) * temp.pop()
        n+=1
    return answer
print(solution(45))