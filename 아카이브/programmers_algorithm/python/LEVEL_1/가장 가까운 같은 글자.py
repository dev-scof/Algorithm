def solution(s):
    answer = []
    for i in range(len(s)):
        idx=i
        for j in range(i-1, -1, -1):
            if s[i]==s[j]:
                idx=j
                break
        if i==idx:
            answer.append(-1)
        else:
            answer.append(i-idx)
    return answer

print(solution("banana"))