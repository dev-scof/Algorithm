a=[]
for _ in range(9):
    a.append(int(input()))
Max = max(a)
print(Max)
print(a.index(Max)+1)