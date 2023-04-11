def solution(n, m, section):
    answer = 0
    '''
    n미터 벽,
    구역을 나누어 일부만 페인트를 칠할거야
    1~n번으로 붙이고, 다시 칠해야할 구역을 정함
    m: 롤러의 길이

    롤러가 벽에서 벗어나면 안된다.
    구역의 일부분만 포함되도록 칠하면 안된다. <?

    '''
    start = section[0]
    for i in range(1, len(section)):
        if section[i]>=start+m:
            answer+=1
            start=section[i]
    else:
        answer+=1
    return answer

# print(solution(8, 4, [2,3,6]))
# print(solution(5, 4, [1,3]))
print(solution(4, 1, [1,2,3,4]))