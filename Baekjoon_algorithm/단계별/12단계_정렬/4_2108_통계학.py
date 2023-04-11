from sys import stdin
from collections import Counter
input = stdin.readline
n = int(input())
data=[]
for i in range(n):
    data.append(int(input()))
data.sort()
avg = round(sum(data)/n)
med = data[int(n/2)]
range_ = max(data)-min(data)
data = Counter(data) # 최빈값을 구하기 위해 Counter 객체 생성
# 출력
print(avg)
print(med)
# 최빈값 처리
data = sorted(data.items(), key=lambda x:x[0], reverse=True) # 숫자에 따라 정렬
data = sorted(data, key=lambda x:x[1], reverse=True)
if n==1: # 숫자 하나일경우
    print(data[0][0])
else:
    mod = [x[0] for x in data if x[1]==data[0][1]]
    if len(mod)==1:
        print(mod[0])
    else:
        mod.sort()
        print(mod[1])
print(range_)