'''

3번의 기회
single double triple 영역
점수는 제곱으로

옵션으로 스타상, 아차상이 있다
스타상 : 해당 점수와 바로 전에 얻은 점수를 2배로 만든다. 해당점수*2 + 이전에 얻은 점수 *2


아차상 : 해당 점수는 마이너스 됨


1S2D*3T => (1^1 + 2^2)*2 + 3^3


1S*2T*3S 
-> 1^1 : 1
-> True, 1^1 : 1 + 1
-> 2^3 : 1+1+8
-> True, 1^1 + 2^3 : 1+1+8+1+8
-> 3^1 : 1+1+8+1+8+3=
= 1                      1
= 1*2                    2
= 1*2 + 2^3              10            
= (1*2 + 2^3) * 2        20
= (1*2 + 2^3) * 2 + 3^1  23
= 4 16 3,
1S*은 1S가 해당점수를 말한다.

'''
def solution(dartResult):
    answer = 0
    score_list = []
    score = ''
    for i in dartResult:
        if i == 'S':
            score_list.insert(0, int(score)) # 앞에 삽입

            score = ''
        elif i == 'D':
            score_list.insert(0, pow(int(score), 2)) # 앞에 삽입
            
            score = ''
        elif i == 'T':
            score_list.insert(0, pow(int(score), 3)) # 앞에 삽입
            
            score = ''
        elif i == '#':
            score_list[0] *= -1

        elif i == '*':
            for i in range(2):
                score_list[i] *= 2
                if len(score_list) ==1:
                    break
        else : # 숫자일 경우
            score = score + i
            print(int(score))
            
    answer = sum(score_list)
    return answer
# 오 댔다
print(solution('1D#2S*3S'))
