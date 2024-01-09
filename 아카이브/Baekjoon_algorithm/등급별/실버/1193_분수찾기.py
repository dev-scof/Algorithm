x=int(input())

line = 0 # 사선라인이 몇번째인지
max_num = 0 # x의 라인에서 가장 큰 숫자
while x > max_num: 
    line+=1
    max_num+=line

gap = max_num-x # 가장 큰 숫자에서 얼만큼 떨어져있는지
if line%2 == 0:
    print(f'{line-gap}/{gap+1}')
else:
    print(f'{gap+1}/{line-gap}')


x=int(input())
line=0
max_num=0
while x>max_num:
    line+=1
    max_num+=line
gap=max_num-x
if line%2==0:
    print()