answer = 0


def dfs(numbers, cur_array, target):
    global answer
    if not numbers:
        if sum(cur_array) == target:
            answer += 1
        return
    dfs(numbers[1:], cur_array + [numbers[0]], target)
    dfs(numbers[1:], cur_array + [-numbers[0]], target)


def solution(numbers, target):
    dfs(numbers, [], target)
    return answer


if __name__ == '__main__':
    # print(solution([1, 1, 1, 1, 1], 3))
    print(solution([4, 1, 2, 1], 4))