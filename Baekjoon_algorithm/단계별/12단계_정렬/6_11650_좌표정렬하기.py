from sys import stdin
n = int(stdin.readline())
points=[]
for _ in range(n):
    points.append(tuple(map(int, stdin.readline().split())))
for i, j in sorted(points, key=lambda x:(x[0], x[1])):
    print(i, j)