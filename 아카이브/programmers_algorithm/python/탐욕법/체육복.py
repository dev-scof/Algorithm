def solution(n, lost, reserve):
    student = [0 for i in range(n)]
    for i in lost:
        student[i-1] -= 1
    for i in reserve:
        student[i-1] += 2
    
    for i in range(n):
        if student[i] ==2: # 여분이 있는경우
            if i-1>=0 and student[i-1] == -1 : # i의 앞에 접근할 수 있고 앞의 번호가 도둑 맞을 경우
                student[i-1]+=1 # 받음
                student[i]-=1 # 줌
            elif i+1<n and student[i+1] == -1: # i의 뒤에 접근할 수 있고, 뒤의 번호가 도둑 맞을 경우
                student[i+1]+=1 #받음
                student[i+1]-=1 #줌
        elif student[i] == -1: # 체육복이 없는 경우
            if i-1>=0 and student[i-1] == 2: # i의 앞에 접근할 수 있고, 앞의 번호가 여분이 있는 경우
                student[i-1] -=1 # 줌
                student[i]+=1 #받음
            elif i+1<n and student[i+1] == 2: # i의 뒤에 접근할 수 있고, 뒤의 번호가 여분이 있는 경우
                student[i+1] -=1 #줌
                student[i]+=1 #받음
    answer = 0
    for i in student:
        if i>=0: # 체육복이 있는 학생인 경우 -> count
            answer+=1
    return answer

print(solution(3, [1,2], [2,3]))