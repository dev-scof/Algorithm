N = int(input())
have=set(input().split())
M = int(input())
cards = input().split()
for card in cards:
    if card in have:
        print(1, end=' ')
    else:
        print(0, end=' ')