from collections import Counter
TC = int(input())
for _ in range(TC):
    counter = Counter()
    num_cloth = int(input())
    for i in range(num_cloth):
        cloth_name, type = input().split()
        counter[type]+=1
    answer=1
    for type, cnt in counter.items():
        answer*=(cnt+1)
    print(answer-1)
