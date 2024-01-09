def solution(a, b):
    week = [ "WED","THU","FRI","SAT","SUN","MON","TUE"]
    day = 1
    month = 1
    while month < a:
        if month == 1:
            day+=31
        elif month == 2:
            day+=29
        elif month == 3:
            day+=31
        elif month == 4:
            day+=30
        elif month == 5:
            day+=31
        elif month == 6:
            day+=30
        elif month == 7:
            day+=31
        elif month == 8:
            day+=31
        elif month == 9:
            day+=30
        elif month == 10:
            day+=31
        elif month == 11:
            day+=30
        elif month == 12:
            break
        month +=1
    
    day += b
    print(day)
    answer = week[day%7]
    return answer

print(solution(1,1))