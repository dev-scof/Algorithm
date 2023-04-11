from collections import Counter
def solution(nums):
    count = Counter(nums)
    if len(nums)/2 > len(count):
        return len(count)
    else:
        return int(len(nums)/2)
print(solution([3,3,3,2,2,4]))