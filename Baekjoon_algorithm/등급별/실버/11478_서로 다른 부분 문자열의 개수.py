from itertools import combinations
s = input()
se = set()
for i in range(len(s)):
    for j in range(i, len(s)):
        se.add(s[i:j+1])
print(len(se))