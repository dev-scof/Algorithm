n = input()
for i in range(int(n)+1):
    m = int(i)
    for j in str(i):
        m+=int(j)
    if int(n)==m:
        print(i)
        break
else:
    print(0)