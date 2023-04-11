import sys
'''
수학적 접근이 필요한 문제
https://pangsblog.tistory.com/62 참고

'''
def gcd(a, b):
    if a%b==0:
        return b
    return gcd(b, a%b)
num = []
for _ in range(int(sys.stdin.readline())):
    num.append(int(sys.stdin.readline()))
num.sort()

# m 구하기
m = num[1]-num[0]
for i in range(2, len(num)):
    m = gcd(m, num[i]-num[i-1])

# m의 약수 구하기
answer = set()
for i in range(1, int(m**0.5)+1):
    if m%i==0:
        answer.add(i)
        answer.add(m//i)
answer.remove(1)
for n in sorted(list(answer)):
    print(n, end=' ')