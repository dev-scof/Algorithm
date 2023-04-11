# 크로아티아 알파벳
input = input()
i = answer = 0
length = len(input)
while i < length:
    if i+1 < length and input[i] == 'c' and input[i+1] =='=':
        answer+=1
        i+=2
    elif i+1 < length and input[i] == 'c' and input[i+1] =='-':
        answer+=1
        i+=2
    elif i+1 < length and input[i] == 'd' and input[i+1] =='-':
        answer+=1
        i+=2
    elif i+1 < length and input[i] == 'l' and input[i+1] =='j':
        answer+=1
        i+=2
    elif i+1 < length and input[i] == 'n' and input[i+1] =='j':
        answer+=1
        i+=2
    elif i+1 < length and input[i] == 's' and input[i+1] =='=':
        answer+=1
        i+=2
    elif i+1 < length and input[i] == 'z' and input[i+1] =='=':
        answer+=1
        i+=2
    elif i+2 < length and i <= length-2 and input[i] == 'd' and input[i+1] =='z' and input[i+2] == '=':
        answer+=1
        i+=3
    else:
        answer+=1
        i+=1
print(answer)

''' 다른 사람 풀이
replace를 사용한 풀이이다.
크로아티아 알파벳에 해당하는 문자를 *로 바꾸어 하나의 문자로 처리하는 방법이다.

S=str(input())
T = ['c=' ,'c-','dz=','d-','lj','nj','s=','z=']
for i in T:
    S=S.replace(i,'*')
print(len(S))
'''