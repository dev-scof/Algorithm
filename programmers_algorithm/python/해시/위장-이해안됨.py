import collections

def solution(clothes):
    answer = 1
    
    cloth = collections.defaultdict(int)
    for i in clothes:
        cloth[i[1]]+=1
    for re in cloth.values():
        answer*=(re+1)
    return answer-1

print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))