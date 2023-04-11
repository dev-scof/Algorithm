from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    
    for k in course: # course에 반복
        candidates = []
        for order in orders:
            for menu in combinations(order, k): # order에 대해 조합을 수행한 것에 대해 반복
                temp = ''.join(sorted(menu))
                candidates.append(temp)
        # candidates에는 가능한 조합들이 중복되어 들어가있다.
        sorted_candidates = Counter(candidates).most_common()
        # Counter.most_common() - 중복된 값들에 대한 카운트를 하는데, ('값', 개수)로 정렬함
        # print('candate = ', candidates)
        # print('sorted = ', sorted_candidates)
        for menu, cnt in sorted_candidates:
            if cnt > 1 and cnt == sorted_candidates[0][1]:
                answer.append(menu)
            
    return sorted(answer)
print("*"*30)
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print("*"*30)
#print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print("*"*30)
#print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))