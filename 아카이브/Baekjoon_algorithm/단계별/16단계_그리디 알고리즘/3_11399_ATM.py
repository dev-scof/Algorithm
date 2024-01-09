# ATM
N = int(input())
P = list(map(int, input().split()))
P.sort()
total=0
for i in range(len(P)):
    total+=sum(P[:i+1])
print(total)