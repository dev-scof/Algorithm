def solution(record):
    user2name = {}
    op = []
    for r in record:
        temp = r.split()
        if temp[0] == 'Enter':
            user2name[temp[1]] = temp[2]
            op.append((temp[1], '님이 들어왔습니다.'))
        elif temp[0] == 'Leave':
            op.append((temp[1], '님이 나갔습니다.'))
        else:
            user2name[temp[1]] = temp[2]
    for i in range(len(op)):
        op[i] = user2name[op[i][0]] + op[i][1]
    return op


if __name__ == '__main__':
    print(solution(
        ["Enter uid1234 Muzi",
        "Enter uid4567 Prodo",
        "Leave uid1234",
        "Enter uid1234 Prodo",
        "Change uid4567 Ryan"]
    ))