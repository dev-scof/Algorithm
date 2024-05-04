def solution(x, y, n):
    """
    x부터 시작, y로 변환
    1. x에 n더하기
    2. x에 2곱하기
    3. x에 3곱하기
    """
    INF = 1e9
    dp = [INF] * (y + 1)
    dp[x] = 1
    for i in range(x, y):
        if dp[i] == 0:
            continue
        if i + n <= y:
            dp[i + n] = min(dp[i + n], dp[i] + 1)
        if i * 2 <= y:
            dp[i * 2] = min(dp[i * 2], dp[i] + 1)
        if i * 3 <= y:
            dp[i * 3] = min(dp[i * 3], dp[i] + 1)
    answer = dp[y] - 1

    if answer == INF - 1:
        answer = -1
    return answer

if __name__ == '__main__':
    print(solution(10, 40, 5)) # 2
    print(solution(10, 40, 30)) # 1
    print(solution(2, 5, 4)) # -1