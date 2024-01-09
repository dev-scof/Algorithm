'''
리스트 : 맞춰야하는 공들의 위치
리스트에 담긴 각 위치에 순서대로 공을 놓아가며 원쿠션 연습을 한다.
이때 머쓱이는 항상 같은 위치에 공을 놓고 쳐서 리스트에 담긴 위치에 놓인 공을 맞춘다.
머쓱이가 친 공이 목표로한 공에 맞을때까지 얼마의 거리를 굴러가야하는지 궁금해졌다.

당구대의 가로길이 m
세로길이 n

머쓱이가 쳐야하는 공이 놓인 위치 : startX, startY
'''
def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls:
        x, y = ball
        position = []
        if not (startX==x and startY>y):
            # 하에 대칭
            position.append((x, -y))
        if not (startX>x and startY==y):
            # 좌에 대칭
            position.append((-x, y))
        if not (startX==x and startY<y):
            # 상에 대칭
            position.append((x, 2*n-y))
        if not (startX<x and startY==y):
            # 우에 대칭
            position.append((2*m-x, y))
        res = []
        for pos in position:
            res.append(((startX-pos[0])**2+(startY-pos[1])**2))
        answer.append(min(res))
    return answer

print(solution(10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]]))