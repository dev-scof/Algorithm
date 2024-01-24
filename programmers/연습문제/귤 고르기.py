from collections import Counter
def solution(k, tangerine):
    counter = Counter(tangerine)
    answer = 0
    for key, value in counter.most_common():
        k-=value
        answer += 1
        if k<=0:
            break

    return answer

if __name__ == '__main__':
    print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
    print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))
    print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))