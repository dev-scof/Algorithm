def solution(n):
    answer = []
    number = 1
    size=0
    for i in range(n):
        line = []
        line.append(number)
        size += number
        number+=1
        answer.append(line)
    line = n-1
    left = 1
    dir = 2
    
    while number <= size:
        if dir == 1: # 아래
            line+=1
            while answer[line][0] > len(answer[line]) and number <= size:
                answer[line].insert(left, number)
                number+=1
                line+=1
            dir=2
            line-=1
            left+=1
        if dir == 2: # 오른
            temp_left=left
            while len(answer[line]) < answer[line][0] and number <= size:
                answer[line].insert(temp_left, number)
                number+=1  
                temp_left+=1
            dir = 3
            line-=1

        if dir == 3 : #위쪽
            while answer[line][0] > len(answer[line]) and number <= size:
                answer[line].insert(left,number)
                number+=1
                line-=1
            dir=1
            line+=1
    
    result=[]
    for i in answer:
        result+=i
    return result
    
print(solution(6))