from collections import Counter
result = sorted(Counter(input().upper()).items(), key=lambda x:x[1])
answer1=result.pop()
if result == []:
    print(answer1[0])
else:
    answer2=result.pop()
    if answer1[1]==answer2[1]:
        print('?')
    else:
        print(answer1[0])