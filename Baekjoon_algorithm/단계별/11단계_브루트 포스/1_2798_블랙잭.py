N, M = map(int, input().split())
cards = list(map(int, input().split()))
Max = 0
for i in range(len(cards)):
    for j in range(i+1, len(cards)):
        for k in range(j+1, len(cards)):
            cur_value = cards[i]+cards[j]+cards[k]
            if cur_value > Max and cur_value <= M:
                Max=cur_value
print(Max)