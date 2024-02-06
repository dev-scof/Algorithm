def solution(n, left, right):
    answer = []
    arr = range(1, n+1)
    rpt, cnt = 1, 0
    for i in range(n):
        rpt_cnt=0
        for j in range(n):
            if left <= cnt <= right:
                if rpt_cnt < rpt:
                    answer.append(arr[i])
                else:
                    answer.append(arr[j])
            rpt_cnt += 1
            cnt += 1
        rpt += 1

    return answer

if __name__ == '__main__':
    print(solution(3, 2, 5))
    print(solution(4, 7, 14))

'''
[
    [1,2,3,4]
    [2,2,3,4]
    [3,3,3,4]
    [4,4,4,4]
]
'''