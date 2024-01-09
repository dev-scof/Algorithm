import sys
input = sys.stdin.readline
n, r, c = map(int, input().strip().split())

ans=0

while n != 0:

    n-=1

    # 왼쪽 상단에 존재할 경우
    if r < 2**n and c < 2**n:
        ans += (2**n) * (2**n) * 0
    
    # 오른쪽 상단에 존재할 경우
    elif r < 2**n and c >= 2**n:
        ans += (2**n) * (2**n) * 1
        c -= (2**n)

    # 왼쪽 하단에 존재할 경우
    elif r >= 2**n and c < 2**n:
        ans += (2**n) * (2**n) * 2
        r -= (2**n)

    # 오른쪽 하단에 존재할 경우
    else:
        ans += (2**n) * (2**n) * 3
        r -= (2**n)
        c -= (2**n)
print(ans)