li=[]
for _ in range(int(input())):
    k=int(input())
    li.pop() if k==0 else li.append(k)
print(sum(li))
