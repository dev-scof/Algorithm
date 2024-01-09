from collections import defaultdict
from itertools import combinations
def duplicateCheck(key, relation):
    for cur_idx in range(len(relation)):
        for check_idx in range(len(relation)):
            if cur_idx == check_idx:
                continue
            cur_value=[]
            check_value=[]
            for col in key:
                cur_value.append(relation[cur_idx][col])
                check_value.append(relation[check_idx][col])
            if cur_value==check_value:
                return False
    return True

def solution(relation):
    answer = []
    duplicate_key = set()
    keys = defaultdict(list)
    # 하나의 속성이 후보키가 되는 키 찾기
    for row in relation:
        for i in range(len(row)):
            if row[i] in keys[i]:
                duplicate_key.add(i)
            keys[i].append(row[i])
    for i in range(len(relation[0])):
        if i not in duplicate_key:
            answer.append((i, ))

    for i in range(2, len(duplicate_key)+1):
        keys = list(combinations(duplicate_key, i))
        for key in keys:
            # print('전달된 키 : ', key)
            # 유일성 체크
            if duplicateCheck(key, relation):
                # 최소성 체크
                flag = True
                for ans in answer:
                    # print('비교할 것 = ', ans, key)
                    if set(ans).issubset(set(key)):
                        flag = False
                        break
                if flag:
                    answer.append(key)

        # print(keys)
    return len(answer)

print(solution([
    ["100","ryan","music","2"],
    ["200","apeach","math","2"],
    ["300","tube","computer","3"],
    ["400","con","computer","4"],
    ["500","muzi","music","3"],
    ["600","apeach","music","2"]
]))