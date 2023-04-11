def solution(n):
    answer = ''
    temp = [1,2,4]

    while n > 0:
        n-=1
        i = n%3
        answer = str(temp[i]) + answer
        n= int(n/3)
    return answer

print(solution(6))
