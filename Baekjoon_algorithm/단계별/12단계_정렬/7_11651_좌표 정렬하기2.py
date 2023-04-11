from sys import stdin
n = int(stdin.readline())
points=[]
for _ in range(n):
    points.append(tuple(map(int, stdin.readline().split())))
for i, j in sorted(points, key=lambda x:(x[1], x[0])):
    print(i, j)