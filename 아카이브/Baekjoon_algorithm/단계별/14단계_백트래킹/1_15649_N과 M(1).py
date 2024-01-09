from sys import stdin, stdout
from itertools import permutations
N, M = map(int, stdin.readline().split())
numbers = [i for i in range(1, N+1)]
for n in list(permutations(numbers, M)):
    for l in n:
        stdout.write(str(l)+" ")
    stdout.write("\n")

'''
from itertools import permutations

N, M = map(int, input().split()) # N, M 입력
li = map(str, range(1, N+1)) # 각각을 문자열로 바꿈
print('\n'.join(list(map(' '.join, permutations(li, M))))) 

**코드 이해**

from itertools import permutations

N, M = map(int, input().split()) # N, M 입력
li = map(str, range(1, N+1)) # 각각을 문자열로 바꿈
temp = list(map(' '.join, permutations(li, M))) # 순열로 된 것을 문자열 처리
print("temp = ", temp)
print('\n'.join(temp))
'''
'''
dfs를 활용

# 15649
n,m = list(map(int,input().split()))
s = []
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
dfs()

'''