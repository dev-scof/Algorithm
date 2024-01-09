import sys
from collections import Counter
input = sys.stdin.readline
input()
card_list = Counter((map(int, input().split())))
input()
for num in list(map(int, input().split())):
    print(card_list.get(num, 0), end=' ')
