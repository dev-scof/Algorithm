from collections import deque
from math import ceil
def solution(fees, records):
    answer = {}
    records = deque(records)
    stack = []
    while records:
        record = records.popleft()
        time, car_num, act = record.split()
        h, m = map(int, time.split(':'))
        time = h*60+m
        if act == 'IN':
            stack.append((car_num, time))
            if car_num not in answer:
                answer[car_num]=0
        else:
            for i in range(len(stack)):
                if stack[i][0]==car_num:
                    break
            in_car_num, in_time = stack.pop(i)
            answer[car_num] += time-in_time
    while stack:
        in_car_num, in_time = stack.pop()
        answer[in_car_num] += 23*60+59 - in_time
    res = []
    keys = sorted(answer.keys())
    for key in keys:
        cost = fees[1]
        if answer[key] > fees[0]:
            cost+= ceil((answer[key]-fees[0])/fees[2])*fees[3]
        res.append(cost)
    return res