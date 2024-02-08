def solution1(citations):
    citations.sort(reverse=True)
    n = len(citations)
    for i in range(n):
        h = citations[i]
        if i+1 >= h:
            break
    return i+1


def solution(citations):
    citations.sort(reverse=True)
    n = len(citations)
    for i in range(n):
        if citations[i] <= i:
            return i
    return n


if __name__ == '__main__':
    print(solution([3, 0, 6, 1, 5]))
    print(solution([10000]))