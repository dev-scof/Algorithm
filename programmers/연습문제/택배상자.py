from collections import deque


def solution(order):
    answer = 0
    stack = []
    order = deque(order)
    for num in range(1, len(order) + 1):
        stack.append(num)
        while stack and stack[-1] == order[0]:
            stack.pop()
            order.popleft()
            answer += 1

    return answer

if __name__ == '__main__':
    print(solution([4, 3, 1, 2, 5]))
    print(solution([5, 4, 3, 2, 1]))