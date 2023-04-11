from itertools import permutations
def solution(numbers):
    numberlist = list(numbers)
    answer = []
    for i in range(1, len(numberlist)+1):
        answer += list(map(''.join, permutations(numberlist, i)))
    
    answer = list(set(map(int, answer)))
    #print('answer = ',answer)
    cnt=0
    for n in answer:
        flag=True
        if n==1 or n==0:
            continue
        for j in range(2, (n//2)+1):
            if n%j==0:
                flag = False
                break
        if flag:
            #print("n = ", n)
            cnt+=1
    return cnt
    '''
    answer = []
    for i in numberlist:
        result = ''
        result += i # result의 맨 앞자리수
        rest_list = numberlist.copy()
        rest_list.remove(i) # i가 선택되었으므로, 삭제
        if result not in answer:
            answer.append(result)
        while True:
            for j in rest_list[:]:
                temp_result = result+j # 
                if temp_result in answer: # 있을경우 패스
                    continue
                else: #없을경우
                    answer.append(temp_result) # answer에 추가
                    rest_list.remove(j) # j가 선택되었으므로 삭제
                    result = temp_result
            if len(result) == len(numberlist):
                break
    print("중복제거 전 = ", answer)
    answer = list(set(list(map(int, answer))))
    cnt = 0
    print(answer)
    
    '''

print(solution("222"))