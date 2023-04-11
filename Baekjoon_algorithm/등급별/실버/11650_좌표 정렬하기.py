point=[]
for _ in range(int(input())):
    point.append(tuple(map(int, input().split())))
point.sort(key=lambda x:(x[0], x[1]))
for p in point:
    print(' '.join(map(str, p)))