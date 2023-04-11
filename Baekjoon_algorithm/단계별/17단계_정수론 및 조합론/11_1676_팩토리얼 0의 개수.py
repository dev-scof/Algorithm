'''
숫자 뒤에 0이 있다는 것은 10이 곱해져 있는 것이다. 
10은 2와 5의 곱으로 이루어지므로 두 수의 개수의 최소 값이 10이 곱해지는 횟수가 된다
https://jaeryo2357.tistory.com/53
'''
num = int(input())
two=five=0 # 2, 5의 개수
for i in range(1, num+1):
    n=i
    # while n%2==0:
    #     two+=1
    #     n//=2
    while n%5==0:
        five+=1
        n//=5
print(five)