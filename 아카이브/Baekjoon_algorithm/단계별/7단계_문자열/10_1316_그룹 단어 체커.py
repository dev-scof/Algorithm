# 그룹 단어 체커
def GroupWord(Str):
    wordList = []
    for c in Str:
        if c not in wordList:
            wordList.append(c)
        elif c != wordList[-1]:
            return 0
    return 1
answer = 0
for i in range(int(input())):
    answer += GroupWord(input())
    
print(answer)
