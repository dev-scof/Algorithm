input()
A = set(map(int, input().split()))
input()
X = list(map(int, input().split()))
for x in X:
    print(1) if x in A else print(0)