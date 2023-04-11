s = input()
flag=True
if len(s)%2==1:
    f = len(s)//2
    b = len(s)//2+1
else:
    f = len(s)//2
    b = len(s)//2
if ''.join(reversed(s[:f]))==s[b:]:
    print(1)
else:
    print(0)