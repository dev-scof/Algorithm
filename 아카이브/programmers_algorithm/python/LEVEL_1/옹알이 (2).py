def solution(babbling):
    answer = 0
    bab={
        'aya':'1',
        'ye':'2',
        'woo':'3',
        'ma':'4'

    }
    for babb in babbling:
        for k in bab:
            if k in babb:
                babb = babb.replace(k, bab[k])
        if babb.isdigit():
            prev_ch=babb[0]
            flag=True
            for i in range(1, len(babb)):
                if babb[i]==prev_ch:
                    flag=False
                    break
                prev_ch=babb[i]
            if flag:
                answer+=1
    return answer

print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))