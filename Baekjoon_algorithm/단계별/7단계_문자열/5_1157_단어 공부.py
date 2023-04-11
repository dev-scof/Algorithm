# 단어 공부
String=input().upper()
alpha = {}
for i in set(String):
    alpha[i] = String.count(i)
max = max(alpha.values())
if list(alpha.values()).count(max) > 1:
    print("?")
else:
    for a, c in alpha.items():
        if c == max:
            print(a)
            break