def solution(arr1, arr2):
    answer = []
    for ar1 in arr1:
        temp = []
        for j in range(len(arr2[0])):
            temp.append(sum(list(map(lambda x: x[0]*x[1], zip(ar1, [x[j] for x in arr2])))))
        answer.append(temp)
    return answer