'''
과제는 시작하기로 한 시각이 되면 시작한다.
새로운 과제를 시작할 시간이 되었을 때, 기존에 진행중이던 과제가 있다면, 진행 중이던 과제를 멈추고 과제를 시작한다.
진행중이던 과제를 끝냈을 때, 잠시 멈춰둔 과제가 있다면, 멈춰둔 과제를 이어서 진행한다.
    - 만약, 과제를 끝낸 시각에 새로 시작해야 되는 과제와 잠시 멈춰둔 과제가 모두 있다면 새로 시작해야하는 과제부터 진행한다.
'''
from collections import deque
from datetime import datetime, timedelta
def solution(plans):
    answer=[]
    plans=deque(sorted(map(lambda x:[x[0],datetime.strptime(x[1], '%H:%M'),x[2]], plans), key=lambda x:x[1]))
    waiting_queue = deque([])

    while plans:
        # [과목, 시작 시간, 작업 시간]
        cur_plan = plans.popleft()
        cur_plan[2] = int(cur_plan[2])
        if not plans:
            answer.append(cur_plan[0])
            while waiting_queue:
                answer.append(waiting_queue.pop()[0])
            break
        next_plan = plans[0]
        next_plan[2] = int(next_plan[2])
        
        # 현재 작업이 끝나는 시간
        cur_plan_fin_time = cur_plan[1]+timedelta(minutes=cur_plan[2])

        # 현재 작업이 다음 작업 시간을 넘어갈 경우 -> wait에 추가
        if cur_plan_fin_time > next_plan[1]:
            waiting_queue.append([cur_plan[0], (cur_plan_fin_time - next_plan[1]).seconds//60])
        # 현재 작업이 다음 작업 시간을 안 넘어갈 경우 -> wait의 작업 수행하기
        else:
            answer.append(cur_plan[0])
            # 헷갈리지 않도록, 재정의
            cur_time = cur_plan_fin_time
            while waiting_queue:
                wait_plan = waiting_queue.pop()
                cur_time += timedelta(minutes=wait_plan[1])
                if cur_time > next_plan[1]:
                    waiting_queue.append([wait_plan[0], (cur_time - next_plan[1]).seconds//60])
                    break
                else:
                    answer.append(wait_plan[0])
    return answer

# print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))
print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
# print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))