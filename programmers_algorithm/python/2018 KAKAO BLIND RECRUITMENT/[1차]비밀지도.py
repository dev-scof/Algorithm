def expressMap(n, num):
    Map = list(bin(num))
    Map = Map[2:]
    while len(Map)<n:
        Map.insert(0, 0)
    return Map

def solution(n, arr1, arr2):
    answer = []
    Map1 = []
    Map2 = []
    for i in arr1:
        Map1.append(expressMap(n, i))
    for i in arr2:
        Map2.append(expressMap(n, i))

    for i in range(n):
        temp = ""
        for j in range(n):
            if int(Map1[i][j]) or int(Map2[i][j]):
                temp += "#"
            else:
                temp += " "
        answer.append(temp)
    return answer
    
print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))