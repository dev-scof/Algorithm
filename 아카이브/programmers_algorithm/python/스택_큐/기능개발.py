import math

def solution(progresses, speeds):
    answer = []
    maxday = 0
    cntday = 0
    result = []
    for i in zip(progresses, speeds):
        day = answer.append(math.ceil((100-i[0])/i[1])) # 걸리는 시간

    maxday = answer[0]
    for i in answer[:]:
        if i>maxday:
            result.append(cntday)
            maxday = i
            cntday = 0
        if i<=maxday:
            cntday +=1
            answer.pop(0)
    if cntday != 0:
        result.append(cntday)
    return result
    
print(solution([93, 30, 55], [1, 30, 5]))
'''
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0] < -((p-100)//s): 
            # Q가 비어있거나, 
            # Q의 마지막 원소의 걸린시간이 현재 원소의 걸리는 시간보다 작은경우
            # 즉, 현재 원소의 걸린 시간이 더 크면 마지막에 삽입.
            Q.append([-((p-100)//s),1])
        else: # day 추가
            Q[-1][1]+=1
    print(Q)
    return [q[1] for q in Q]
'''