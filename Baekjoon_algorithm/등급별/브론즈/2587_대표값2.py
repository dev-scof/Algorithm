ar = []
for _ in range(5):
    ar.append(int(input()))
ar.sort()
print(sum(ar)//len(ar))
print(ar[len(ar)//2])