def solution(w,h):
    line = 1
    x = max(w, h)
    y = min(w, h)
    grad = y/x
    answer = 0
    for i in range(1, x+1):
        if grad * i >= line:
            answer += x - i
            line+=1
    return answer*2
print(solution(8,3))