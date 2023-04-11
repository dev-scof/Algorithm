import datetime as dt
from math import ceil
def solution(fees, records):
    cars = dict()
    acc = dict()
    for i in records:
        time, num, stat = i.split(' ')
        if stat == 'IN':
            cars[num] = dt.datetime.strptime(time, "%H:%M")
            if num not in acc:
                acc[num]=0 #0으로 초기화
        else: #OUT이면 시간 누적하기
            #print("*"*12)
            startTime = cars[num]
            LastTime = dt.datetime.strptime(time, "%H:%M")
            t =  LastTime - startTime
            t = t.seconds/60
            # print("자동차 번호 = ", num)
            # print("시작 시간 = ", startTime)
            # print("끝 시간 = ", LastTime)
            # print("주차 시간 = ", t)            
            acc[num] += t
            del(cars[num])
    if cars: # OUT이 없을경우 -> 23:59 로 계산, 순서대로 계산되므로, 삭제할 필요없음
        #print("OUT 없음")
        for num, time in cars.items():
            startTime = time
            LastTime = dt.datetime.strptime("23:59", "%H:%M")
            t =  LastTime - startTime
            t = t.seconds/60
            # print("자동차 번호 = ", num)
            # print("시작 시간 = ", startTime)
            # print("끝 시간 = ", LastTime)
            # print("주차 시간 = ", t)
            acc[num] += t
    '''계산'''
    for num, time in acc.items():
        if time <= fees[0]:
            acc[num] = fees[1] # 기본요금 청구
        else:
            acc[num] = fees[1] + ceil((time - fees[0])/fees[2])*fees[3]
    
    # print("&*&*&*")
    # print(acc)
    answer = [x[1] for x in sorted(acc.items(), key=lambda x:x[0])]

    return answer
print(
    solution(
        [180, 5000, 10, 600], # 기본 시간 / 기본 요금 / 단위 시간 / 단위 요금
        ["05:34 5961 IN", 
        "06:00 0000 IN", 
        "06:34 0000 OUT", 
        "07:59 5961 OUT", 
        "07:59 0148 IN", 
        "18:59 0000 IN", 
        "19:09 0148 OUT", 
        "22:59 5961 IN", 
        "23:00 5961 OUT"]))