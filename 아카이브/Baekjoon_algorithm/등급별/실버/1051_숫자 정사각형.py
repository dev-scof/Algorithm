n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, list(input()))))
length=min(n, m)
i=j=0
while length>0:
    
    if i+length>=n:
        i=0
        j=0
        length-=1
        continue
    if j+length>=m:
        i+=1
        j=0
        continue
    if arr[i][j]==arr[i+length][j]==arr[i+length][j+length]==arr[i][j+length]:
        break
    j+=1
print((length+1)**2)