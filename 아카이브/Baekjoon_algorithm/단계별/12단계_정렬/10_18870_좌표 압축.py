from sys import stdin, stdout
input = stdin.readline
N = int(input())
Xpoints = list(map(int, input().split()))
sorted_Xpoints = {v: k for k, v in enumerate(sorted(set(Xpoints)))} # 인덱스 값과 키 위치를 변경
for x in Xpoints:
    stdout.write(str(sorted_Xpoints[x])+ " ")
