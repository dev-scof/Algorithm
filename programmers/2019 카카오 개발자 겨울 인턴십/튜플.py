def solution(s):
    answer = []
    elements = sorted(s[2:-2].split('},{'), key= lambda x:len(x))
    for element in elements:
        for elem in element.split(','):
            num = int(elem)
            if num not in answer:
                answer.append(num)
    return answer

if __name__ == '__main__':
    print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
    print(solution("{{20,111},{111}}"))