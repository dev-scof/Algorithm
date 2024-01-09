from itertools import product
def solution(word):
    alpha = 'AEIOU'
    dic = []
    for i in range(5):
        dic+=(list(map(''.join, map(list, product(alpha, repeat=i+1)))))
    return list(sorted(dic)).index(word)+1

print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))
