def solution(n):
    answer = 0
    temp = []
    while n>0:
        temp.append(n%3)
        n= n//3
    temp.reverse()
    three = 1
    for i in temp:
        answer += i*three
        three*=3
    return answer
print(solution(45))
'''
3  45
   15  0
   5   0
   1   2

1 2 0 0
0 0 2 1
'''
