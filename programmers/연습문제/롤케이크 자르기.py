from collections import Counter

def solution(topping):
    answer = 0
    counter = Counter(topping)
    L = set() # 앞부분
    l_cnt = 0

    for topp in topping:
        counter[topp] -= 1
        if topp not in L:
            L.add(topp)
            l_cnt += 1
        if counter[topp] == 0:
            del counter[topp]
        if l_cnt == len(counter):
            answer += 1
    return answer




def solution2(topping): # 999초
    answer = 0
    a = set()
    while topping:
        a.add(topping.pop(0))
        if len(a) == len(set(topping)):
            answer += 1
    return answer

def solution1(topping): # 2222초
    answer = 0
    for i in range(1, len(topping)):
        if len(set(topping[:i])) == len(set(topping[i:])):
            answer += 1
    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))  # 2
print(solution([1, 2, 3, 1, 4]))  # 0
