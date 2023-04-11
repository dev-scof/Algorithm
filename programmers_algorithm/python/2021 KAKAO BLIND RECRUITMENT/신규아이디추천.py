import re
def solution(new_id):
    answer = new_id.lower() # 1단계
    answer = re.sub('[^-_.\da-z]+', '', answer) # 2단계
    answer = re.sub("[.*]{2,}", ".", answer) # 3단계
    if answer[0]=='.': # 4단계
        answer = answer[1:]
    if answer == "": # 5 단계
        answer="a"
    if answer[len(answer)-1] == '.': # 4 단계
        answer = answer[:len(answer)-1]
    if len(answer) >= 16: # 6단계
        answer = answer[:15]
    if answer[len(answer)-1] == '.': # 6단계, 마지막 마침표 제거
        answer = answer[:len(answer)-1]
    
    while len(answer)<3 :
        answer += answer[len(answer)-1]
    
    return answer

print(solution("z-+.^."))