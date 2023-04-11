def solution(s, n):
    answer = ''
    S = list(s)
    for i, value in enumerate(S):
        if value>='a' and value<='z': #소문자인 경우
            answer += chr((ord(value)+n-ord('a'))%26+ord('a'))
        elif value>='A' and value<='Z': #대문자인 경우
            answer += chr((ord(value)+n-ord('A'))%26+ord('A'))
        elif value == ' ':
            answer += ' '
    return answer
print(solution("a B z", 4))

'''
isupper()
islower()
메소드를 사용하는 방법도 있다.
'''