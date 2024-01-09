N = int(input())
distance=list(map(int, input().split()))
price=list(map(int, input().split()))
min_price=price[0]
cost=0

for i in range(len(distance)):
    # 가격이 적을경우
    if price[i]<min_price:
        min_price=price[i]
    cost+=distance[i]*min_price
    
print(cost)