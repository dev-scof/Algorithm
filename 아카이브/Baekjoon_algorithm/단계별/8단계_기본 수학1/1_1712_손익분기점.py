# 손익분기점
A, B, C = list(map(int, input().split()))
answer = A
if B >= C:
    print(-1)
else:
    print(int(A/(C-B))+1)
        