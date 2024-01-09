from bisect import bisect_left
def solution(sequence, k):
    max_sum=0
    end=0
    res = []
    for i in range(len(sequence)):
        while max_sum <k and end < len(sequence):
            max_sum += sequence[end]
            end += 1
        if max_sum == k:
            res.append([i, end-1])
        max_sum-=sequence[i]
    res = sorted(res, key=lambda x:x[1]-x[0])

    return res
print(solution([1, 2, 3, 4, 5], 7))
print(solution([1, 1, 1, 2, 3, 4, 5], 5))
print(solution([2, 2, 2, 2, 2], 6))