# 분수찾기
# https://codesyun.tistory.com/58
# 왜 n에서 i를 빼고, i를 증가시키는가?
n = int(input())
i=1
while n>i:
    n-=i
    i+=1
if i%2==1:
    print(str(i+1-n)+'/'+str(n))
else:
    print(str(n)+'/'+str(i+1-n))
