def solution(numbers):
    numberlist = []
    for i in numbers:
        numberlist.append([str(i)*5, i])
    numberlist.sort(reverse=True, key=lambda x:x[0])
    answer = [i[1] for i in numberlist]
    
    answer = ''.join(list(map(str,answer)))

    if int(answer) == 0:
        return '0'
    else:
        return answer
    
print(solution([0,0,0,0,0]))

'''
from itertools import permutations
def solution(numbers):
    answer = permutations(numbers)
    
    result = []
    for i in answer:
        result.append(int(''.join(map(str, list(i)))))
    
    #return str(max(result))
print(solution([6,10,2]))
'''