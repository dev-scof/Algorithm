import sys
input = sys.stdin.readline
N = int(input())
dp = []
for _ in range(N):
    dp.append(list(map(int, input().split())))
for i in range(1, N):
    for j in range(len(dp[i])):
        if j==0:
            dp[i][j]+=dp[i-1][0]
        elif j==len(dp[i])-1:
            dp[i][j]+=dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])+dp[i][j]
print(max(dp[N-1]))
'''
                                7
                            3       8
                        8       1       0
                    2       7       4       4
                4       5       2       6       5

7 3 8 7 5 => 30


RGB거리 풀이와 비슷한 흐름인 것을 파악
'''