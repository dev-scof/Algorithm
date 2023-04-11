# 이진탐색(재귀)
def binary_search_recur(array, target, start, end):
    # 시작점이 끝점을 넘어갈 경우 -> 탐색 종료
    if start>end:
        return None
    
    # mid값 지정
    mid = (start+end) // 2

    # 타겟을 찾은 경우
    if array[mid] == target:
        return mid

    # 타겟보다 큰 경우 -> 왼쪽 탐색
    elif array[mid] > target:
        return binary_search_recur(array, target, start, mid-1)

    # 타겟보다 작은 경우 -> 오른쪽 탐색
    else:
        return binary_search_recur(array, target, mid+1, end)

# 이진탐색(반복문)
def binary_search_loop(array, target, start, end):
    while start <= end:
        # mid 값 지정
        mid = (start + end) // 2

        # 타겟을 찾은 경우
        if array[mid] == target:
            return mid
        # 타겟보다 큰 경우 -> 왼쪽 탐색 (s ~ mid-1)
        elif array[mid] > target:
            end = mid-1
        # 타겟보다 작은 경우 -> 오른쪽 탐색 (mid+1 ~ e)
        else:
            start = mid+1

from bisect import bisect_left
def binary_search_bisect(array, target):
    return bisect_left(array, target)

array = [1,3,5,7,9,11,13,15,17,19]
# 위 배열에서 7의 위치(index)를 탐색
print(binary_search_recur(array, 7, 0, len(array)-1))
print(binary_search_loop(array, 7, 0, len(array)-1))
print(binary_search_bisect(array, 7))