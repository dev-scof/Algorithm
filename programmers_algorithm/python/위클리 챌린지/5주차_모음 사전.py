from itertools import permutations
def solution(word):
    answer = 0
    alpha = ['A', 'E', 'I', 'O', 'U',
    'A', 'E', 'I', 'O', 'U',
    'A', 'E', 'I', 'O', 'U',
    'A', 'E', 'I', 'O', 'U',
    'A', 'E', 'I', 'O', 'U']
    dictionary = set()
    for i in range(1, 6):
        for j in permutations(alpha, i):
            t = ''.join(j)
            dictionary.add(t)
    return sorted(list(dictionary)).index(word)+1
print(solution("AAAE"))
'''
product 를 사용한다면 더욱더 좋았을 것 같다
from itertools import product

solution = lambda word: sorted(
    ["".join(c) for i in range(5) for c in product("AEIOU", repeat=i+1)]).index(word) + 1

'''
'''
A E I O U



A       1
AA      2
AAA     3
AAAA    4
AAAAA   5
AAAAE   6
AAAAI   7
AAAAO   8
AAAAU   9
AAAE    10
AAAEA   11
AAAEE   12



'''