def solution(numbers):
    '''
    서로다른 인덱스에 있는 두개의 수를 더해서 만들 수 있는 모든 수를 오름차순으로 담는다.
    '''
    answer = set()
    for i, value1 in enumerate(numbers):
        for j, value2 in enumerate(numbers):
            if i == j:
                continue
            add_two_num = value1+value2
            answer.add(add_two_num)
    answer = list(answer)
    answer.sort()
    return answer

print(solution([2,1,3,4,1]))