'''
d[i] : 마지막으로 뽑은 수가 a[i]일 때, 가장 긴 부분수열의 길이
'''
N = int(input())

List = list(map(int, input().split()))

dp = [1]*1000

for i in range(N):
    print('현재 i = ', i, List[i])
    for j in range(i):
        print('비교한다 j = ', j, List[j])
        if List[i] > List[j]:
            print(f'List[i]({List[i]}) > List[j]({List[j]})')
            dp[i] = max(dp[i], dp[j]+1)
    print('dp = ', dp[:N+1])
    print()
            
print(max(dp))