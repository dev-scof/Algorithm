from math import ceil
def solution(progresses, speeds):
    answer, max_day = [], 0
    tasks = 1
    for progress, speed in zip(progresses, speeds):
        day = ceil((100-progress) / speed)
        # 배포해야할 때
        if max_day < day:
            max_day = day
            answer.append(tasks)
            tasks = 1
        # 기다릴 때
        else:
            tasks += 1
    if tasks:
        answer.append(tasks)
    return answer[1:]

if __name__ == '__main__':
    # print(solution([93, 30, 55], [1, 30, 5]))
    # print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
    # print(solution([1, 95, 95, 95], [99, 1, 1, 1]))
    # print(solution([99, 98], [1, 1]))
    print(solution([99, 96, 94], [1, 3, 4]))