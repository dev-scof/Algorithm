def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    for i in arr:
        if answer == [] :
            answer.append(i)
        elif answer[-1] != i:
            answer.append(i)
        
    print(answer)
    return answer
print(solution([1,1,3,3,0,1,1]))

