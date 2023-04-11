for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dis = (pow((x1-x2),2)+pow((y1-y2),2))**0.5
    if dis==0:
        if r1==r2:
            print(-1)
        else:
            print(0)
    elif abs(r1-r2) < dis and dis < abs(r1+r2):
        print(2)
    elif r1+r2 == dis or abs(r1-r2) == dis:
        print(1)
    elif x1==x2 and y1==y2 and r1==r2:
        print(-1)
    else:
        print(0)
    