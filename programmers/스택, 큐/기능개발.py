def solution(progresses, speeds):
    answer = []
    max_days = 0
    tasks = 1
    for progress, speed in zip(progresses, speeds):
        day = (100-progress) // speed
        if max_days == 0:
            max_days = day
        elif max_days < day: # 스택을 비워야할 경우
            answer.append(tasks)
            tasks = 1
        else:
            tasks += 1
    else:
        answer.append(tasks)
    return answer

if __name__ == '__main__':
    print(solution([93, 30, 55], [1, 30, 5]))
    print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))