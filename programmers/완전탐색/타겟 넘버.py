answer = 0


def dfs1(numbers, cur_array, target):
    global answer
    if not numbers:
        print(cur_array)
        if sum(cur_array) == target:
            answer += 1
        return
    number = numbers.pop(0)
    dfs1(numbers, cur_array + [number], target)
    dfs1(numbers, cur_array + [-number], target)
    numbers.append(number)

def dfs(numbers, cur_array, target):
    global answer
    if not numbers:
        if sum(cur_array) == target:
            answer += 1
        return
    dfs(numbers[1:], cur_array + [numbers[0]], target)
    dfs(numbers[1:], cur_array + [-numbers[0]], target)


def dfs2(numbers, cur_array, target):
    # 이 코드도 가능함.
    global answer
    if not numbers:
        print(cur_array)
        if sum(cur_array) == target:
            answer += 1
        return
    number = numbers.pop(0)
    dfs2(numbers, cur_array + [number], target)
    dfs2(numbers, cur_array + [-number], target)
    numbers.insert(0, number)


def solution(numbers, target):
    dfs2(numbers, [], target)
    return answer


if __name__ == '__main__':
    # print(solution([1, 1, 1, 1, 1], 3))
    print(solution([4, 1, 2, 3], 4))