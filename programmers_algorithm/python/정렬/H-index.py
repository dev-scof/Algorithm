def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    # 6 5 3 1 0
    # n개 중 h번 인용된 논문이 h편 이상
    # 나머지 논문이 h 이하인데
    # 처음에 6이 h가 되고, len(cation[:i+1])이 h 이상 사용된 논문의 갯수이고
    # 나머지 갯수는 len(cation)-i-1이 h 이하 사용된 논문의 갯수이다.
    n = len(citations)
    for i in range(n):
        h= citations[i]
        if i+1 >= h:
            # i+1 : 현재 갯수
            break

    return i+1
print(solution([3,0,6,1,5]))

'''
def solution(citations):
    citations.sort() # 정렬
    len_citations = len(citations) # 길이

    for i in range(len_citations):
        if len_citations - i <= citations[i]: 
            # len_citations - i : 남은 갯수
            # citations[i] : h
            # 남은 갯수가 h 이하 남을때 브레이크..
            break

    if i + 1 == len_citations:
        return 0
    else:
        return len_citations - i

if name == "main":
    print(solution([0, 0, 0]))
'''