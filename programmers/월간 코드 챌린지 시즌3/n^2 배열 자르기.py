def solution(n, left, right):
    answer = []
    while left <= right:
        l, c, = divmod(left, n)
        if c < l+1:
            answer.append(l+1)
        else:
            answer.append(c+1)
        left += 1
    return answer

if __name__ == '__main__':
    # print(solution(3, 2, 5))
    # print(solution(4, 7, 14))
    print(solution(5, 7, 23))

'''
[
    [1,2,3,4]
    [2,2,3,4]
    [3,3,3,4]
    [4,4,4,4]
]
'''