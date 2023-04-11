def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'
def solution(scores):
    answer=''
    for i in range(len(scores)):
        temp = []
        for j in range(len(scores)):
            temp.append(scores[j][i])
        if scores[i][i] ==  max(temp) or scores[i][i] == min(temp):
            if temp.count(scores[i][i]) != 1:
                answer += grade(sum(temp)/len(temp))
            else:
                answer += grade((sum(temp) - scores[i][i])/(len(temp)-1))
        else:
            answer += grade(sum(temp)/len(temp))
    return answer
print(solution([
    [100,90,98,88,65],
    [50,45,99,85,77],
    [47,88,95,80,67],
    [61,57,100,80,65],
    [24,90,94,75,65]
    ]))