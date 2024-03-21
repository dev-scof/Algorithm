def solution(msg):
    # msg의 길이는 1 글자 이상, 1000 글자 이하
    answer = []
    cache = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    idx = 0
    w = ''
    while idx < len(msg):
        w += msg[idx]
        idx += 1
        if w not in cache:
            cache.append(w)
            answer.append(cache.index(w[:-1])+1)
            w = w[-1]
    answer.append(cache.index(w)+1)
    return answer


if __name__ == '__main__':
    print(solution("KAKAO"))
    print(solution("TOBEORNOTTOBEORTOBEORNOT"))
    print([20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34])
    print(solution("ABABABABABABABAB"))
