def solution(N, stages):
    Error = []
    for i in range(N):
        pass_ = 0
        for j in stages:
            if i+1 <= j :# i스테이지를 하고있거나 지나간 수
                pass_ +=1
        if pass_==0:
            ErrorRate = (i+1, 0)
        else:
            ErrorRate = (i+1, stages.count(i+1) / pass_)
        Error.append(ErrorRate)
    
    Error.sort(key = lambda Error:Error[1], reverse=True)
    answer = []
    for i in Error:
        answer.append(i[0])
    return answer

print(solution(5, [2,1,2,6,2,4,3,3]))