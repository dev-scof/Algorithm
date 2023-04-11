# 
import sys
input = sys.stdin.readline
T = int(input())
P = [0,1,1,1,2,2]

for _ in range(T):
    N = int(input())
    if N >= len(P):
        # P가 계산되지 않았을 경우
        while True:
            if len(P)>N:
                break
            P.append(P[len(P)-1]+P[len(P)-5])
    print(P[N])