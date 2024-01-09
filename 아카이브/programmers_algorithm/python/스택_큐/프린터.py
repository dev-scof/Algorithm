def solution(priorities, location):
    answer = 0
    queue = []
    
    #location은 인덱스
    for i, value in enumerate(priorities):
        temp = [i, value]
        queue.append(temp)
    while queue != []:
        flag = False
        temp = queue.pop(0) # 첫번째꺼 뽑고
        for value in queue:
            if temp[1] < value[1]: # 중요도가 큰 값이 있으면
                queue.append(temp) # 뒤에 삽입
                flag = True # 뒤에 박혔음을 알려줌
                break
        if flag:
            continue
        else:
            answer+=1
        if temp[0] == location:
            break
    return answer
print(solution([1, 1, 9, 1, 1, 1], 0))