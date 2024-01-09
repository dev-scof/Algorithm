N, C = map(int, input().split())
home = [int(input().rstrip()) for _ in range(N)]
home.sort()
s = 1 # 공유기 사이의 가장 짧은 거리
e = home[-1]-home[0] # 공유기 사이의 가장 긴 거리
while s <= e:
    mid = (s+e)//2 # 가장 인접한 공유기 사이의 거리 정하기
    value=home[0] # 첫번째 집에는 무조건 설치,
    count=1
    # 현재 mid로 설치할 수 있는 공유기 개수 구하기
    for i in range(1, N):
        # 공유기 사이의 거리가 넘어갈 경우 -> 공유기 설치
        if home[i] >= value + mid:
            count+=1
            value=home[i]
    if count>=C:
        s=mid+1
    else:
        e=mid-1
print(e)