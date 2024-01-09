def solution(x):
    answer = True
    num = x
    rest = []
    while x > 0:
        rest.append(x%10)
        x=int(x / 10)
    
    S = sum(rest)
    if num % S ==0:
        return True
    else:
        return False

print(solution(11))