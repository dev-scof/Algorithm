'''
햄버거에 들어갈 재료를 조리해주면 
-> 조리된 순서대로 아래서부터 위로 쌓인다.
-> 따로 옮겨 포장한다.

정해진 순서 : 빵-야채-고기-빵

[야채, 빵, 빵, 야채, 고기, 빵, 야채, 고기, 빵, 야채, 고기, 빵]
-> 스택

숫자형 리스트에서 슬라이스 연산을 하면 시간이 오래걸린다.
스택을 문자열로 처리하면 연산부분에서 더 빨라지는것같다?
'''
def solution(ingredient):
    ingredient=''.join(map(str, ingredient))
    answer = 0
    stack = ''
    for ingred in ingredient:
        stack+=ingred
        if stack[-4:] == '1231':
            answer+=1
            stack=stack[:-4]

    return answer
print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))