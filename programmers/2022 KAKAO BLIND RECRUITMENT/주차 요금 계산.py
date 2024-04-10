from collections import defaultdict
from datetime import datetime


def solution(fees, records):
    acc_time = defaultdict(int) # 차 번호당 주차 누적 시간
    park_status = defaultdict()

    # 1. 차량에 대한 누적 시간 계산
    for record in records:
        time, num, stat = record.split()
        if stat == 'IN':
            park_status[num] = datetime.strptime(time, "%H:%M")
        else:  # OUT이면 시간 누적
            start_time = park_status[num]
            end_time = datetime.strptime(time, "%H:%M")
            t = (end_time - start_time).seconds // 60  # 분 단위로 전환
            acc_time[num] += t
            del park_status[num]  # 주차장을 나갔으므로 삭제

    # 아직 주차장을 나가지 않은 차량에 대한 정산 처리
    for num, time in park_status.items():
        start_time = time
        end_time = datetime.strptime("23:59", "%H:%M")
        t = (end_time - start_time).seconds // 60  # 분 단위로 전환
        acc_time[num] += t

    # 2. 누적 시간에 대한 주차 요금 계산
    for num, time in acc_time.items():
        if time <= fees[0]:
            acc_time[num] = fees[1]  # 기본 요금 청구
        else:
            acc_time[num] = fees[1] + ((time - fees[0] - 1) // fees[2] + 1) * fees[3]
    # 3. 차량 번호로 정렬
    answer = [acc_time[num] for num in sorted(acc_time.keys())]

    return answer


if __name__ == '__main__':
    print(solution(
        [180, 5000, 10, 600], # 기본 시간, 기본 요금, 단위 시간, 단위 요금
        ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
    ))
    print(solution(
        [120, 0, 60, 591],
        ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
    ))
    print(solution(
        [1, 461, 1, 10],
        ["00:00 1234 IN"]
    ))
