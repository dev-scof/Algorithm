from collections import Counter
ar=[]
for _ in range(int(input())):
    ar.append(int(input()))
print(int(round(sum(ar)/len(ar), 0)))
sorted_ar=list(sorted(ar))
print(sorted_ar[len(ar)//2])
counter = Counter(ar)
ans=[]
common = max(counter.values())
for k, v in counter.items():
    if v==common:
        ans.append(k)
if len(ans)!=1:
    ans.sort()
    print(ans[1])
else:
    print(ans[0])
print(sorted_ar[-1]-sorted_ar[0])