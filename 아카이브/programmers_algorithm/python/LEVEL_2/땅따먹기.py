def solution(land):
    answer= 0
    n = len(land)
    for i in range(n-1):
        land[i+1][0] += max(land[i][1],land[i][2],land[i][3])
        land[i+1][1] += max(land[i][0],land[i][2],land[i][3])
        land[i+1][2] += max(land[i][0],land[i][1],land[i][3])
        land[i+1][3] += max(land[i][0],land[i][1],land[i][2])
        
    return land[n-1]

print(solution([
    [1,2,3,5],
    [5,6,7,100],
    [4,3,2,1]
    ])) # 5 7 4 -> 16