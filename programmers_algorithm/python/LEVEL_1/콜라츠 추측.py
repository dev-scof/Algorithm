def solution(num):
    cnt = 0
    for i in range(500):
        if num == 1:
            break
        if num%2==0:
            num = int(num/2)
            cnt+=1
        else:
            num *= 3
            num +=1
            cnt+=1
    if cnt==500:
        return -1
    else:
        return cnt

print(solution(16))