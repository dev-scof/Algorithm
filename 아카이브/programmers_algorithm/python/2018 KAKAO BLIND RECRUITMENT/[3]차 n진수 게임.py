def ex(r):
    if r == 10:
        return 'A'
    elif r == 11:
        return 'B'
    elif r == 12:
        return 'C'
    elif r == 13:
        return 'D'
    elif r == 14:
        return 'E'
    elif r == 15:
        return 'F'
    else:
        return str(r)
def notation(num, n):
    temp = []
    q, r = divmod(num, n)
    temp.append(ex(r))
    while q > 0:
        q, r = divmod(q, n)
        temp.append(ex(r))
    return temp
def solution(n, t, m, p):
    answer = ''
    num=0
    ba_list = []
    cur_p = 0
    p-=1
    while len(answer) < t:
        if ba_list == []: # 리스트가 비어있으면
            ba_list = notation(num, n)
            num+=1
        if cur_p%m == p: # 순서이면
            answer+=ba_list.pop()
        else:
            ba_list.pop()
        cur_p+=1 # 순서 더하기
    return answer

## 인덱스를 활용하여 효율적으로 푼다면?
def notation2(num, n):
    temp = []
    q, r = divmod(num, n)
    temp.append(ex(r))
    while q > 0:
        q, r = divmod(q, n)
        temp.append(ex(r))
    temp.reverse()
    return temp
def solution2(n, t, m, p):
    answer = ''
    num=0
    ba_list = []
    cur_p = 0
    p-=1
    while len(ba_list) < t*m+1:
        if cur_p >= len(ba_list):
            ba_list += notation2(num, n)
            num+=1
        cur_p+=1
    print(ba_list)
    for i in range(t):
        answer += ba_list[i*m+p]
    return answer           

print(solution2(16,16,2,1))