'''
과제는 시작하기로 한 시각이 되면 시작한다.
새로운 과제를 시작할 시간이 되었을 때, 기존에 진행중이던 과제가 있다면, 진행 중이던 과제를 멈추고 과제를 시작한다.
진행중이던 과제를 끝냈을 때, 잠시 멈춰둔 과제가 있다면, 멈춰둔 과제를 이어서 진행한다.
    - 만약, 과제를 끝낸 시각에 새로 시작해야 되는 과제와 잠시 멈춰둔 과제가 모두 있다면 새로 시작해야하는 과제부터 진행한다.
'''
from collections import deque
from datetime import datetime, timedelta
def solution(plans):
    # [과목, 시작 시간, 작업 시간]
    plans=list(map(lambda x:[x[0],datetime.strptime(x[1], '%H:%M'),x[2]], plans))
    for plan in plans:
        plan.append(plan[1]+timedelta(minutes=int(plan[2])))
    

    return ""

print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))
print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))