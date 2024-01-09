num = int(input())
n=cnt=1
while True:
    if n>=num:
        break
    n+=cnt*6
    cnt+=1
print(cnt)