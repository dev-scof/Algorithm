def solution(answers):
    first = [1,2,3,4,5] # 5
    second = [2,1,2,3,2,4,2,5] # 8
    third = [3,3,1,1,2,2,4,4,5,5] #10
    len_answers = len(answers)
    c_f = c_s = c_t = 0
    for i, value in enumerate(answers):
        if value == first[i % len(first)]:
            c_f += 1
        if value == second[i % len(second)]:
            c_s += 1
        if value == third[i % len(third)]:
            c_t += 1

    max_ = max(c_f, c_s, c_t)
    answer = []
    if max_ == c_f:
        answer.append(1)
    if max_ == c_s:
        answer.append(2)
    if max_ == c_t:
        answer.append(3)
    return answer

solution([1,3,2,4,2])