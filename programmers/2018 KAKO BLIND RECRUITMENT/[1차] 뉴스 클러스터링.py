from collections import Counter
def jacard_set(s):
    result = []
    for i in range(len(s)):
        elem = s[i:i+2]
        if elem.isalpha() and len(elem) == 2:
            result.append(elem.lower())
    return result
def solution(str1, str2):
    a_set, b_set = jacard_set(str1), jacard_set(str2)
    if not a_set and not b_set:
        return 65536
    # 다중 처리
    a_c = Counter(a_set)
    b_c = Counter(b_set)
    return int((sum((a_c&b_c).values()) / sum((a_c|b_c).values()))*65536)

if __name__ == '__main__':
    # print(solution('FRANCE', 'french'))
    # print(solution('handshake', 'shake hands'))
    print(solution('aa1+aa2', 'AAAA12'))
    # print(solution('E=M*C^2', 'e=m*c^2'))

