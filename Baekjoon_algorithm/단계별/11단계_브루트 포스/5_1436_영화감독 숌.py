def is_right(n):
    num = str(n)
    cnt=0
    for i in num:
        if cnt==3:
            return True
        if i=='6':
            cnt+=1
        else:
            cnt=0
    if cnt==3:
            return True
    return False
n = int(input())
k=0
num=666
while k<n:
    if is_right(num):
        k+=1
    num+=1
print(num-1)