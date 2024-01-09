def solution(n):
    return int(''.join(sorted(list(str(n)), reverse=True)))

print(solution(118372))
'''
def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))

n을 str로 바꾸고 list로 바꿈
리스트를 sort함
join하여 int형으로 반환

def solution(n):
    return int("".join(sorted(list(str(n)), reverse=True)));

join에도 reverse=True의 속성이 있음을 알 수 있다.
'''