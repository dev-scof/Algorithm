def solution(want, number, discount):
    answer = 0
    want_number = list(zip(want, number))
    for i in range(len(discount)-9):
        flag=True
        for want, number in want_number:
            if discount[i:i+10].count(want)<number:
                flag=False
                break
        if flag:
            answer+=1
    return answer