def solution(s):
    answer=0
    i=0
    while i<len(s):
        x_cnt=1
        a_cnt=0
        for j in range(i+1, len(s)):
            if x_cnt==a_cnt:
                idx=j
                answer+=1
                break
            if s[i]==s[j]:
                x_cnt+=1
            else:
                a_cnt+=1
        else:
            answer+=1
            break
        i=idx
    return answer
print(solution("banana"))
print(solution("abracadabra"))
print(solution("aaabbaccccabba"))