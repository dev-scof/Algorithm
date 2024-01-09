def solution(phone_number):
    numberlist = list(phone_number)
    answer = ''
    for i in numberlist[:len(numberlist)-4]:
        answer+='*'
    for i in numberlist[len(numberlist)-4:]:
        answer+=i
    return answer
print(solution("01033334444	"))
'''
def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]

문자열의 곱셈을 통해 만들 수 있었다...
'''