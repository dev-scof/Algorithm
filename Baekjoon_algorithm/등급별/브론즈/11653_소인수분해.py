n = int(input())
divisor = []
for i in range(2, n+1):
    if n%i==0:
        divisor.append(i)
d_i=0
while True:
    if d_i>=len(divisor):
        break
    if n%divisor[d_i]==0:
        print(divisor[d_i])
        n/=divisor[d_i]
    else:
        d_i+=1

# ;;;
n = int(input())
for i in range(2, n+1):
    while n%i==0:
        print(i)
        n/=i
