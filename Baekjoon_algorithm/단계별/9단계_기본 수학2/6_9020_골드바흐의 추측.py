prime_list = [True]*(1234567) 
for i in range(2, int(1234567**0.5)+1): 
    if prime_list[i] == True:
        for j in range(i+i, 1234567, i):
            prime_list[j]=False
for _ in range(int(input())):
    n = int(input())
    l = r = int(n/2)
    while not (prime_list[l] == prime_list[r] == True):
        l-=1
        r+=1
    print(l, r)
'''

import sys
n = list(map(int,sys.stdin.readlines()[1:]))
le = max(n)
a = [*range(le + 1)]
a[1] = 0
for i in a:
  if i > 1:
    a[i * i::i] = [0] * (le // i - i + 1)
a = {*a}
for i in n:
  for j in range(i // 2, 1, -1):
    if j in a and i - j in a:
      print(j, i - j)
      break
'''