n, c = map(int, input().split())
home = [int(input().rstrip()) for _ in range(n)]
home.sort()
start = 1
end = home[-1] - home[0]
while start <= end:
    # 가장 인접한 공유기 사이의 거리
    mid = (start + end) // 2
    value=home[0] # 공유기 초기 설치 위치
    count=1 # 공유기 설치 개수
    # 현재 mid로 설치할 수 있는 공유기 개수 구하기
    for i in range(1, n):
        if home[i]>=value + mid:
            count+=1
            value=home[i]
    if count>=c:
        start=mid+1
    else:
        end=mid-1
print(end)