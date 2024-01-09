answer=0
n=input()
cnt=0
for i in range(1, len(n)):
    cnt+=((10**(len(n)-i))-(10**(len(n)-(i+1))))*len(n[i:])
print(cnt+(int(n) - 10 ** (len(n) - 1) + 1) * len(n))
