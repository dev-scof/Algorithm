import math
def solution(n, m):
    gcd = math.gcd(n,m)
    lcm = n*m // gcd
    return [gcd, lcm]
print(solution(3, 12))

'''
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer

유클레드 호제법을 사용
c는 큰수, d는 작은수로 지정

t가 0이 될 때까지 무한루프를 돌림
t = 큰수를 작은수로 나눈 나머지
c = 두번째 수, d는 t로

'''