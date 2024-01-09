from sys import stdin
n = int(input())
roads = list(map(int, input().split()))
oils = list(map(int, input().split()))

res = roads[0] * oils[0] # 답
m = oils[0] # 오일의 최소가격
dist=0 # 거리
for i in range(1, n-1):
    if oils[i] < m: # 현재 오일 가격이 현가격보다 싸면
        res += m*dist # 현가격 * 거리 를 계산하여 더한다. (비용)
        dist = roads[i] # 지금위치로부터 다음까지의 거리로 초기화한다.
        m = oils[i] # 현재 오일 가격으로 업데이트한다.
    else: # 현 가격이 싸면
        dist += roads[i] # 거리만 증가시킨다.
    if i==n-2: # 마지막에 다다르면
        res += m*dist # 현재 제일 싼 값에 거리를 곱하여 더한다.
print(res)


'''
-> 위의 코드를 짧게 구현한 코드 (dist 변수를 지울 수 있다.)

n = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

res = 0
m = costs[0]
for i in range(n-1):
    if costs[i] < m:
        m = costs[i]
    res += m * roads[i]
print(res)
'''