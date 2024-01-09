def solution(n, words):
    _round = 0
    last_alpa = ''
    word_set = set()
    for i, word in enumerate(words):
        if i%n == 0:
            _round +=1
        if last_alpa == '':
            last_alpa = word[-1]
            word_set.add(word)
            continue
        if (
            word[0] != last_alpa
            or word in word_set
        ):
            answer = [i%n+1, _round]
            break
        last_alpa = word[-1]
        word_set.add(word)
    else:
        answer = [0, 0]
    return answer

if __name__ == '__main__':
    print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
    print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
    print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))