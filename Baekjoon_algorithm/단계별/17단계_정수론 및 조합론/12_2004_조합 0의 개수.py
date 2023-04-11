# https://velog.io/@jini_eun/%EB%B0%B1%EC%A4%80-2004%EB%B2%88-%EC%A1%B0%ED%95%A9-0%EC%9D%98-%EA%B0%9C%EC%88%98-Java-Python
import sys
n, m = map(int, sys.stdin.readline().split())

# 5 개수 세는 함수
def five_count(n):
    cnt = 0
    while n != 0:
        n = n // 5
        cnt += n
    return cnt

# 2 개수 세는 함수
def two_count(n):
    cnt = 0
    while n != 0:
        n = n // 2
        cnt += n
    return cnt

if m == 0:
    print(0)  
else:       
    print(min(two_count(n)-two_count(m)-two_count(n-m), five_count(n)-five_count(m)-five_count(n-m)))