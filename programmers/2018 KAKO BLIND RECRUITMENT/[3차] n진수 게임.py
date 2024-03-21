hex = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}

def n진수(n, num):
    if num == 0:
        return [0]
    result = []
    while num:
        num, r = divmod(num, n)
        if r >= 10:
            r = hex[r]
        result = [r] + result
    return result


def solution(n, t, m, p):
    # n진법, 미리 구할 숫자의 개수 t, 게임에 참가하는 인원 m, 튜브의 순서 p
    '''
    미리 구할 숫자의 개수 t * 게임에 참가하는 인원 m까지 구하면 된다.
    2 | 12
      |  6 ... 0
      |  3 ... 0
      |  1 ... 1
      -> 1100
    '''
    answer = []
    num = 0
    while len(answer) <= t*m:
        answer.extend(n진수(n, num))
        num += 1
    return ''.join(map(str, answer[p-1:m*t:m]))
if __name__ == '__main__':
    print(solution(2, 4, 2, 1))
    print(solution(16, 16, 2, 1))
    print(solution(16, 16, 2, 2))