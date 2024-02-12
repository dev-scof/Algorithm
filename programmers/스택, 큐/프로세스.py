from collections import deque
def solution1(priorities, location):
    answer = 0
    priorities = list(enumerate(priorities))
    while priorities:
        idx, priority = priorities.pop(0)
        max_priority = max([p[1] for p in priorities])
        # 현재 프로세스를 실행시켜야할 경우
        if priority >= max_priority:
            answer += 1
            # 알고 싶은 프로세스의 위치 또는 마지막 위치일 경우
            if idx == location or not priorities:
                return answer
        else:
            priorities.append((idx, priority))
    return answer

def solution(priorities, location):
    answer = 0
    priorities = list(enumerate(priorities))
    while priorities:
        idx, priority = priorities.pop(0)
        max_priority = max([p[1] for p in priorities]) if priorities else -1
        # 현재 프로세스를 실행시켜야할 경우
        if priority >= max_priority:
            answer += 1
            # 알고 싶은 프로세스의 위치 또는 마지막 위치일 경우
            if idx == location or not priorities:
                return answer
        else:
            priorities.append((idx, priority))
    return answer

if __name__ == '__main__':
    print(solution([2, 1, 3, 2], 2)) # 1
    print(solution([1, 1, 9, 1, 1, 1], 0)) # 5