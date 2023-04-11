ans=0
for i in range(1, int(input())+1):
    if len(str(i))==1:
        ans+=1
    else:
        d=int(str(i)[0])-int(str(i)[1])
        flag=True
        for j in range(len(str(i))-1):
            if int(str(i)[j]) - int(str(i)[j+1]) != d:
                flag=False
                break
        if flag:
            ans+=1
print(ans)
            

