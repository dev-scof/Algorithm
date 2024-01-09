def solution(s):
    s = ''.join(s[1:-2]).replace('{', '').split('},')
    list_array = []
    for i in s:
        temp = set(map(int, i.split(',')))
        list_array.append(temp)
    list_array.sort(key=lambda x:len(x))
    answer = []
    for i in list_array:
        for j in i:
            if j in answer:
                continue
            else:
                answer.append(j)
    
    return answer
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
'''
중복된 원소가 있을 수 있습니다. ex : (2, 3, 1, 2)
원소에 정해진 순서가 있으며, 원소의 순서가 다르면 서로 다른 튜플입니다. ex : (1, 2, 3) ≠ (1, 3, 2)
튜플의 원소 개수는 유한합니다.

2           {a1}
2 1         {a1, a2}         // a2 = {1}
2 1 3       {a1, a2, a3}     // a3 = {3}
2 1 3 4     {a1, a2, a3, a4} // a4 = {4}
'''