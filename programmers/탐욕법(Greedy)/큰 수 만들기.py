from collections import deque


def solution(number, k):
    numbers = deque(map(int, list(number)))
    stack = [numbers.popleft()]
    for n in numbers:
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)

    if k != 0:
        stack = stack[:-k]
    return ''.join(map(str, stack))


if __name__ == '__main__':
    print(solution("1924", 2)) # "94"
    print(solution("1231234", 3)) # "3234"
    print(solution("4177252841", 4)) # "775841"
