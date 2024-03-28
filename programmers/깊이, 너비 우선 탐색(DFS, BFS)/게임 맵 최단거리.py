from collections import deque
def solution(maps):
    q = deque([(0, 0)])
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    max_i = len(maps)
    max_j = len(maps[0])
    while q:
        ci, cj = q.popleft()
        for k in range(4):
            mi = ci + di[k]
            mj = cj + dj[k]
            if 0 <= mi < max_i and 0 <= mj < max_j and maps[mi][mj] == 1:
                maps[mi][mj] = maps[ci][cj] + 1
                q.append((mi, mj))
    return maps[max_i-1][max_j-1] if maps[max_i-1][max_j-1] != 1 else -1


if __name__ == '__main__':
    print(solution([
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1]]
    )) # 11
    print(solution([
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1]
    ])) # -1