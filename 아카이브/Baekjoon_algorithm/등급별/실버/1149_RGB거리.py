N = int(input())
house=[]
for _ in range(N):
    house.append(list(map(int, input().split())))
for i in range(1, len(house)):
    # i번째집을 빨강으로 칠했을 때의 최솟값
    house[i][0] = min(house[i-1][1], house[i-1][2]) + house[i][0]

    # i번째집을 초록으로 칠했을 때의 최솟값
    house[i][1] = min(house[i-1][0], house[i-1][2]) + house[i][1] 
    
    # i번째집을 파랑으로 칠했을 때의 최솟값
    house[i][2] = min(house[i-1][0], house[i-1][1]) + house[i][2]
print(min(house[N-1][0], house[N-1][1], house[N-1][2]))
'''
오답노트
line 7 : house[i][0] = min(house[i-1][1], house[i-1][2]) + house[i][0]
# house[i-1][1] : 이전에 초록으로 칠했을 때의 최솟값
# house[i-1][2] : 이전에 파랑으로 칠했을 때의 최솟값
'''