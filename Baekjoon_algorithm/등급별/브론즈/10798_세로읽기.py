a=[]
for i in range(5):
    s = list(input())
    if a==[]:
        a=s
    else:
        for j in range(len(s)):
            if j > len(a)-1:
                a.append(s[j])
            else:
                a[j]+=s[j]
print(''.join(a))