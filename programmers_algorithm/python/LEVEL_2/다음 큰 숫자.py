def solution(n):
    answer = n+1
    # n의 다음 숫자
    # n보다 큰 자연수
    # n의 다음 숫자의 2진변환했을때의 1의 갯수 == n을 2진변환했을때 1의 갯수
    n_bin_countOne = bin(n).count('1')
    for i in range(n+1, 1_000_000):
        answer_bin_countOne = bin(answer).count('1')
        if answer_bin_countOne == n_bin_countOne:
            break
        answer+=1
    return answer

print(solution(78))