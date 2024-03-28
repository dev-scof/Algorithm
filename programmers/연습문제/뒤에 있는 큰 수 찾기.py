def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for i, num in enumerate(numbers):
        # 스택에서 빼야할 경우
        while stack:
            if stack[-1][1] < num:
                idx, _ = stack.pop()
                answer[idx] = num
            else:
                stack.append((i, num))
                break
        # 스택에 넣어야할 경우
        else:
            stack.append((i, num))
    return answer


if __name__ == '__main__':
    print(solution([2, 3, 3, 5]))
    print(solution([9, 1, 5, 3, 6, 2]))