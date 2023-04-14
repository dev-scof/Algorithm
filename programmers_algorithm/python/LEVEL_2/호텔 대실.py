from datetime import datetime, timedelta
def solution(book_time):
    book_time = list(sorted(map(lambda x:[ datetime.strptime(x[0], '%H:%M'), datetime.strptime(x[1], '%H:%M')], book_time), key=lambda x:x[0]))
    rooms = []
    for book in book_time:
        fin_time = book[1]+timedelta(minutes=10)
        if rooms == []:
            rooms.append([fin_time])
        else:
            flag = True
            for room in rooms:
                if room[-1] <= book[0]:
                    room.append(fin_time)
                    flag=False
                    break
            if flag:
                rooms.append([fin_time])
    return len(rooms)

def solution(book_time):
    n = 24 * 60 + 10
    dp = [0] * n

    for t in book_time:
        start, end = t
        s_h, s_m = map(int, start.split(":"))
        e_h, e_m = map(int, end.split(":"))
        dp[s_h*60 + s_m] += 1 # 입실 시간 -> +1
        dp[e_h*60 + e_m + 10] -= 1 # 퇴실 시간+10분 -> -1

    for i in range(n-1):
        # 다음거에 이전값을 더해라,
        # 만약 겹치지 않는다면, 입실시간부터 퇴실시간+10분까지 0이 1로 채워질 것이다.
        # 만약 겹친다면? 1000010000-1 이라고한다면 11111222221 이 될 것이다. // 2부분은 객실이 2개 사용되고 있음을 의미한다.
        # 그러면, 겹치는 시간에 대해 객실의 수가 만들어질 수 있다.
        dp[i+1] += dp[i]

    return max(dp)
print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
# print(solution([["09:10", "10:10"], ["10:20", "12:20"]]))
# print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]))