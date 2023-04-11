import sys
input = sys.stdin.readline
fibo = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
n = int(input())
for i in range(len(fibo), n+1):
    fibo.append(fibo[i-2]+fibo[i-1])
print(fibo[n])