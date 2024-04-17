def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            # 현재 열을 제외한 이전 행의 최대값 계산
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
    return max(land[-1])


if __name__ == '__main__':
    print(solution([
        [1, 2, 3, 5],
        [5, 6, 7, 8],
        [4, 3, 2, 1]
    ]))