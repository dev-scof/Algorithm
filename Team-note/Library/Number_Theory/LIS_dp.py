# 원소가 n개인 배열의 일부 원소를 골라서 만들 수 있는
# 수열의 최대 길이를 구하는 알고리즘
# arr = [10, 20, 10, 30, 20, 50]
input()
arr = list(map(int, input().split()))
dp = [1]*10
def LIS(arr):
    for i in range(len(arr)):
        print('*'*30)
        print('현재 위치 : ', i, arr[i])
        for j in range(i):
            print('비교하는 j = ',j, arr[j])
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
                print('갱신된 dp = ', dp)
LIS(arr)
print(max(dp))
'''
[input]
6
10 20 10 30 20 50

[output]
4
'''

'''
알고리즘 풀이
- 현재 위치에서 이전의 값들과 비교한다.
- 만약 현재 값보다 이전의 값이 작은 경우
    - 이전까지의 최대길이(dp[j]+1)과 현재까지의 최대길이(dp[i]) 중에서 큰 값을 dp[i]에 저장한다.
'''