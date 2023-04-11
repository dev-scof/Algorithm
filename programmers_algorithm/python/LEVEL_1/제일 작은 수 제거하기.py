def solution(arr):
    answer = []
    arr.pop(arr.index(min(arr)))
    return arr if arr!=[] else [-1]
print(solution([10]))