xp = []
yp = []
for _ in range(3):
    x, y = map(int, input().split())
    if x not in xp:
        xp.append(x)
    else:
        xp.remove(x)
    if y not in yp:
        yp.append(y)
    else:
        yp.remove(y)
print(xp[0], yp[0])
'''
이런 방법이?!

x=y=0
for _ in range(3):
    i, j = map(int, input().split())
    x^=i
    y^=j
print(x, y)

'''