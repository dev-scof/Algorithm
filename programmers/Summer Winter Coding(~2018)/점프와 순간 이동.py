def solution(n):
    answer = 0
    while n>0:
        if n%2 == 0:
            n /= 2
        else:
            n -= 1
            answer +=1
    return answer

if __name__ == '__main__':
    print(solution(5))
    print(solution(6))
    print(solution(5000))

# 1
# 1 2
# 1 2 2 3
# 1 2 2 3 2 3 3 4
# 1 2 2 3 2 3 3 4 2 3 3 4 3 4 4 5
