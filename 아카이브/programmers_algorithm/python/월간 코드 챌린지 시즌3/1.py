def solution(numbers):
    return sum([x for x in [1,2,3,4,5,6,7,8,9] if x not in numbers])

print(solution([1,2,3,4,6,7,8,0]))