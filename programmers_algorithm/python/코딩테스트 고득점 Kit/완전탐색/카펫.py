def solution(brown, yellow):
    area = brown+yellow
    # 최소 높이는 3부터
    height = 3
    # 최소 높이에 따른 width
    width = area//height
    while width >= 3:
        if (height-2)*(width-2) == yellow:
            return [width, height]
        height+=1
        width=area//height
print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))