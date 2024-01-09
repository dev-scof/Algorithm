from itertools import permutations
n, m = map(int, input().split())
cards = list(sorted(map(lambda x:sum(x), (permutations(map(int, input().split()), 3)))))
for card in cards:
    if card>m:
        break
    cur=card
print(cur)