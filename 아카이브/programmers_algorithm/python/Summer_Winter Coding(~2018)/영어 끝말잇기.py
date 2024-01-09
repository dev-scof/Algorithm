def solution(n, words):
    answer = []
    duplicate = {}
    count = 1 # 횟수
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    number = 1 # 첫번째 사람
    word = words.pop(0)
    duplicate[word]=0
    first_spell = word[-1]
    for word in words:
        number +=1 # 다음 사람
        if number > n:
            number%=n
            count+=1 # 횟수 증가
        if word[0] != first_spell or (word in duplicate):
            return [number, count]
        else:
            first_spell = word[-1]
            duplicate[word]=0
    return [0,0]
print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))