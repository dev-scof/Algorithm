'''
12분

기사는 1~number까지 번호 지정
기사들이 무기 산대
각 기사는 자신의 기사 번호의 "약수의 개수"에 해당하는 공격력을 가진 무기를 구매하려고 한다.
단, 이웃나라와의 협약에 의해, 공격력의 제한수치를 정하고, 제한수치보다 큰 무기는 협약기관에서 정한 무기를 사야한다.


'''
def divide_cnt(number):
    cnt=0
    if number==1:
        return 1
    for i in range(1, int(number**0.5)+1):
        if number % i ==0:
            cnt+=2
        if i*i==number:
            cnt-=1
    return cnt
def solution(number, limit, power):
    answer=0
    for i in range(1, number+1):
        cnt = divide_cnt(i)
        if cnt>limit:
            answer+=power
        else:
            answer+=cnt
    return answer
print(solution(5, 3, 2))
print(solution(10, 3, 2))