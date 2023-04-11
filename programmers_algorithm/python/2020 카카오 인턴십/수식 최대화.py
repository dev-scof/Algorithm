from collections import deque
from itertools import permutations
def solution(expression):
    # 음수라면 절대값으로 계산
    answer = 0
    answers = []
    numbers = []
    
    number = ""
    for s in expression:
        if s.isdigit():
            number+=s
        else:
            numbers.append(number)
            numbers.append(s)
            number=""

    numbers.append(number)
    #print('numbers = ', numbers)
    
    
    #print(expression)
    numbers = list(map(str, numbers))
    #print(type(numbers[0]))
    # 3중 for문
    opers_types = ["*", "+", "-"]
    for i in range(3):
        for j in range(3):
            if i==j:
                continue
            for k in range(3):
                if j==k or i==k:
                    continue
                cals = numbers.copy()
                #print("우선순위 : ", opers_types[i], ">", opers_types[j], ">", opers_types[k])

                # 첫번째 우선순위
                p = 0
                while cals[:]:
                    #print('test',cals, 'p = ', p, 'len cals = ',len(cals))
                    if p >= len(cals):
                        break
                    
                    if cals[p] == opers_types[i]:
                        cals.insert(p-1, str(eval(''.join(cals[p-1:p+2]))))
                        cals.pop(p)
                        cals.pop(p)
                        cals.pop(p)
                        p-=3
                        #print("join = ", cals)
                    p+=1
                    
                # 두번째 우선순위
                p = 0
                while cals[:]:
                    #print('test',cals, 'p = ', p, 'len cals = ',len(cals))
                    if p >= len(cals):
                        break
                    
                    if cals[p] == opers_types[j]:
                        cals.insert(p-1, str(eval(''.join(cals[p-1:p+2]))))
                        cals.pop(p)
                        cals.pop(p)
                        cals.pop(p)
                        p-=3
                        #print("join = ", cals)
                    p+=1
                
                # 세번째 우선순위
                p = 0
                while cals[:]:
                    #print('test',cals, 'p = ', p, 'len cals = ',len(cals))
                    if p >= len(cals):
                        break
                    
                    if cals[p] == opers_types[k]:
                        cals.insert(p-1, str(eval(''.join(cals[p-1:p+2]))))
                        cals.pop(p)
                        cals.pop(p)
                        cals.pop(p)
                        p-=3
                        #print("join = ", cals)
                    p+=1
                
                # 계산
                answers.append(abs(int(cals[0])))
        #print('answers = ', answers)
                
    return max(answers)

print(solution("100-200*300-500+20"))