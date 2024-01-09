def solution(record):
    user_database = {} # userid : name
    record_database = [] 
    for s in record:
        temp = s.split()
        if temp[0][0] == 'E':
            user_database[temp[1]] = temp[2]
            record_database.append([temp[1], '님이 들어왔습니다.'])
        elif temp[0][0] == 'L':
            record_database.append([temp[1], '님이 나갔습니다.'])
        else:
            user_database[temp[1]] = temp[2]
    answer = []
    for i in record_database:
        answer.append(user_database[i[0]]+i[1])
    return answer
print(solution(
    ["Enter uid1234 Muzi", 
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan"]))