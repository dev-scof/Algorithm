def solution(s, skip, index):
    answer = ''
    for ch in s:
        i=0
        ch_ord = ord(ch)
        while i<index:
            ch_ord+=1
            if ch_ord > ord('z'):
                ch_ord=ord('a')
            
            if chr(ch_ord) in skip:
                continue
            else:
                i+=1
            
        answer+= chr(ch_ord-ord('z') + ord('a')) if ch_ord > ord('z') else chr(ch_ord)

    return answer

print(solution("aukks", "wbqd", 5))
'''
다른 방법 : 
1. a~z까지 할당한 이후, skip에 해당하는 문자를 삭제한다.
2. 이후 index만큼 옮긴것에 대해 answer에 추가한다.
def solution(s, skip, index):
    atoz = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in skip:
        atoz.remove(i)

    ans = ''
    for i in s:
        ans += atoz[(atoz.index(i)+index)%len(atoz)]

    return ans
'''