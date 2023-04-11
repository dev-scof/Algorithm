'''
모든 요청이 배정되어있음 -> 요청한 금액을 그대로 배정
모든 요청이 배정될 수 없음 -> 특정한 정수 상한액 계산, 그 이상인 요청에는 상한액으로 배정
'''
N = int(input())
cost = list(map(int, input().split()))
total_cost = int(input())
def sol(N, costs:list, total_cost):
    costs.sort()
    s=0
    l=costs[-1]
    while s<=l:
        mid = (s+l)//2
        SUM=0
        for cost in costs:
            # 정해진 예산보다 넘어가면 -> 상한액으로 배정
            if cost>=mid:
                SUM+=mid
            # 안넘어가면 그대로 배정
            else:
                SUM+=cost
        # 총액이 정해진 종액보다 크면 -> 줄여야한다.
        if SUM > total_cost:
            l=mid-1
        else:
            s=mid+1
    return l
print(sol(N, cost, total_cost))
# print(sol(4, [120, 110, 140, 150], 485))
# print(sol(5, [70, 80, 30, 40, 100], 450))