def solution(s):
    answer = ''
    cnt = 0
    for i in list(s):
        if i == ' ':
            answer+=' '
            cnt=0
        else: # 문자일 경우
            if cnt%2==0:
                answer += i.upper()
            else:
                answer += i.lower()
            cnt+=1
    return answer
print(solution("try hello world"))