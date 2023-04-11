def solution(s):
    answer = []
    word = s.split(' ')
    
    for i in word:
        i = list(i)
        for j, value in enumerate(i):
            if j==0:
                i[j] = i[j].upper()
            else:
                i[j] = i[j].lower()
        answer.append(''.join(i))
    
    return ' '.join(answer)

print(solution("3people unFollowed me"))