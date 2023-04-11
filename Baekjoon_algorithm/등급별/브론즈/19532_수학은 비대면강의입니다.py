a, b,c,d,e,f = map(int, input().split())
'''
ax + by = c // y = (c-ax)/b
dx + ey = f // x = (f - ec/b)/(d-a/b)
'''
x = (b*f-e*c)//(b*d-e*a)
if b==0:
    y = (f-d*x)//e
else:
    y = (c-a*x)//b
print(x, y)