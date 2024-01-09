text = set()
for _ in range(int(input())):
    text.add(input())
for i in sorted(list(text), key=lambda x: (len(x), x)):
    print(i)