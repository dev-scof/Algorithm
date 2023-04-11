'''
8분
사과를 상태에따라 1~k점으로 준다
- 한 상자에 사과를 m개 담는다.
- 상자에 담긴 사과 중 가장 낮은 점수가 p점인 경우, 사과 한 상자의 가격은 p * m이다.

가능한 사과를 팔았을때, 얻을 수 있는 최대 이익

k=3, m=4면, 
'''
def solution(k, m, score:list):
    score.sort(reverse=True)
    i=0
    answer=0
    while True:
        if i+m>len(score):
            break
        answer+= (m*score[i:i+m][-1])
        i+=m
    return answer
# print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))