from collections import Counter
def solution(str1, str2):
    test = "kdajslkc dkjkd"
    A_list = []
    for i in range(len(str1)):
        temp_str = str1[i:i+2].lower()
        if len(temp_str) <= 1:
            continue
        if temp_str.isalpha(): # 알파벳이면 넣어라
            A_list.append(temp_str)
    A = Counter(A_list)
    B_list = []
    for i in range(len(str2)):
        temp_str = str2[i:i+2].lower()
        if len(temp_str) <= 1:
            continue
        if temp_str.isalpha(): # 알파벳이면 넣어라
            B_list.append(temp_str)
    B = Counter(B_list)
    #print('A = ', A, 'B = ', B)
    AUB = Counter()
    AnB = Counter()
    for i in A:
        if i in B: # A n B
            add_dict = {i : max(A[i], B[i])} # 합집합
            AUB += Counter(add_dict)
            add_dict = {i : min(A[i], B[i])} # 교집합
            AnB += Counter(add_dict)
        else:
            add_dict = {i : A[i]}
            AUB += Counter(add_dict)
    for i in B:
        if i not in AUB: # B에만 존재
            add_dict = {i : B[i]}
            AUB += Counter(add_dict)
    answer = 0
    if sum(AUB.values()) == 0:
        return 65536
    '''
    A = FR AN CE
    B = fr en ch

    print(AUB)
    print("AUB.values", sum(AUB.values()))
    print(AnB)
    print("AnB.values", sum(AnB.values()))
    '''
    return int(sum(AnB.values())/ sum(AUB.values()) * 65536)
print(solution("E Ce", "e ce"))
'''
두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의한다
A = {1,2,3}
B = {2,3,4}
A n B = {2,3}
A U B = {1,2,3,4}
-> 2/4 = 0.5

if A U B = O -> 1로 처리

다중 처리
A = {1,1,1}
B = {1,1,1,1,1}
A n B = {1,1,1}
A U B = {1,1,1,1,1}
-> 3/5

A = {1,1,2,2,3}
B = {1,2,2,4,5}
A n B = {1,2,2}
A U B = {1,1,2,2,3,4,5}
-> 3/7

두 글자씩 끊어 다중집합의 원소로 만든다.
- 영문자로 된것만 유효, 다른 문자가 들어가면 넣지 않는다.
- AB, ab, Ab는 같은 원소 처리한다.

'''
''' 다른 사람 풀이
from collections import Counter
def solution(str1, str2):
    # make sets
    s1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    s2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    if not s1 and not s2:
        return 65536
    c1 = Counter(s1)
    c2 = Counter(s2)
    answer = int(float(sum((c1&c2).values()))/float(sum((c1|c2).values())) * 65536)
    return answer
'''