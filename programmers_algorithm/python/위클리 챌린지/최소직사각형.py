'''
다양한 모양과 크기의 명함을 모두 수납할 수 있으면서
작아서 들고 다니기 편한 지갑


'''


def solution(sizes):
    return max(map(lambda x: x[0] if x[0] > x[1] else x[1], sizes))*max(map(lambda x: x[1] if x[0] > x[1] else x[0], sizes))
    # 정민이
    return max(map(max, sizes)) * max(map(min, sizes))


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
'''
[[60, 50], [30, 70], [60, 30], [80, 40]]	    4000

[[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]	120
[[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]	133
'''