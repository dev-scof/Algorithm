from sys import stdin
cal = stdin.readline().rstrip().split('-')
answer=sum(map(int, cal[0].split('+')))
for c in cal[1:]:
    answer-=sum(map(int, c.split('+')))
print(answer)


'''
arr = input().split('-') 
s = 0 
for i in arr[0].split('+'): 
    s += int(i) 
for i in arr[1:]: 
    for j in i.split('+'): 
        s -= int(j) 
print(s)
'''
'''
오답노트

처음 접근 방법
- +를 묶어서 나중에 빼야하는 숫자에서 모두 빼버리자
- +를 묶는 방법에 있어서 스택을 사용하고 여러 if문 조건을 생각하는 문제 발생
- 다양한 시도를 하던 중 파이썬의 eval함수를 사용하면 괜찮겠다고 생각하여
수식을 만들기 시작했다.
-> 백준에서 eval함수를 막아서인지 SyntaxError가 떴다.
-> 검색

검색후 접근 방법
- 검색을 해보니 문제를 해결하는 방향은 맞았으나 
구현에서 문제가 발생한 것을 알 수 있었다.
- split()함수를 통하여 -, +가 들어간 부분을 쉽게 나눌 수 있었으며
- 숫자를 구분하는 번거로움도 없어졌다.

'''