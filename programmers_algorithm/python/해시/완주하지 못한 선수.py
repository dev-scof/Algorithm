import collections

def solution(participant, completion):
    answer = ''
    p = collections.Counter(participant)
    for i in completion:
        p[i]-=1
        if p[i]<=0:
            p.pop(i)

    return p.popitem()[0]

    #return participant
print(solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']))

''' 다른사람 코드
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

- Counter객체는 뺄셈 연산이 가능하다.

'''