def solution(prices):
    N = len(prices)
    answer = [0] * N
    stack = []

    for i, price in enumerate(prices):
        # stack이 비어있지 않고, 주식 가격이 떨어졌을 경우
        while stack and stack[-1][1] > price:
            idx, _ = stack.pop()
            answer[idx] = i - idx # 주식 가격이 떨어진 시간
        stack.append((i, price)) # (현재 인덱스, 주식 가격)

    # stack에 남아있는 주식 가격은 떨어지지 않은 주식 가격
    for i, price in stack:
        answer[i] = N - i - 1
    return answer


if __name__ == '__main__':
    print(solution([1, 2, 3, 2, 3])) # [4, 3, 1, 1, 0]