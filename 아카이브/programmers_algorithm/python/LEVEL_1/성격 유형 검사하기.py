def solution(survey, choices):
    answer = ''
    score = [3,2,1,0,1,2,3]
    rank={
        'RT' : [0, 0],
        'CF' : [0, 0],
        'JM' : [0, 0],
        'AN' : [0, 0],
    }
    for sury, cho in zip(survey, choices):
        i = cho-1
        if sury in ['TR', 'FC', 'MJ', 'NA']:
            sury = ''.join(list(reversed(sury)))
            if i>3:
                rank[sury][0]+=score[i]
            elif i<3:
                rank[sury][1]+=score[i]
        else:
            if i>3:
                rank[sury][1]+=score[i]
            elif i<3:
                rank[sury][0]+=score[i]
    for k, v in rank.items():
        if v[0] > v[1]:
            answer+=k[0]
        elif v[0] < v[1]:
            answer+=k[1]
        else:
            answer+=list(sorted(k, reverse=True)).pop()
    
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))