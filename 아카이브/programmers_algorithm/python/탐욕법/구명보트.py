'''def solution(people, limit):
    answer = 0
    people.sort()
    f=sum=0
    l = len(people)-1
    for i, value in enumerate(people[:]):
        if people == []:
            break
        sum =value
        people.pop(0)# 첫번째 선택
        answer+=1
        l = len(people)-1
        while l>=0:
            if sum+people[l] <= limit:
                people.pop(l) # 두번째 선택

                break
            l-=1
            
    return answer
'''

def solution(people, limit):
    answer = len(people)
    people.sort()
    s = 0
    e = answer - 1
    while s < e:
        if people[s] + people[e] <= limit:
            s += 1
            answer -= 1
        e -= 1
    return answer
