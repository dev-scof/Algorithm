from collections import Counter
def solution(id_list, report, k):
    report = set(report) # 중복 제거
    rel = [] # 신고 관계, rel[0] : 신고 한 사람, rel[1] : 신고 받은 사람

    answer = [0]*len(id_list)
    for doc in report:
        rel.append(str(doc).split(' '))
    
    count = Counter([x[1] for x in rel]) # 신고 당한 횟수

    for name in count:
        if count[name] >= k: # 정지된 경우
            for i in rel:
                if i[1] == name:
                    answer[id_list.index(i[0])]+=1
                    
    return answer

print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))