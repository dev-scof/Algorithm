'''
6분
1대1, 음식 종류 및 양이 바뀐다.
준비된 음식들을 일렬로 배치
한 선수는 왼쪽부터 오른쪽, 다른 선수는 오른쪽에서 왼쪽
중앙에는 물, 물 먼저 먹는애가 이김

3가지음식, 칼로리가 적은 순서대로 1번 음식을 3개 / 2번음식을 4개, 3번음식을 6개, 
'''

def solution(food):
    answer = ''
    for i, f in enumerate(food):
        if i==0:
            continue
        answer+=str(i)*(f//2)
    answer = answer + '0' + ''.join(reversed(answer))
    return answer

print(solution([1, 3, 4, 6]))