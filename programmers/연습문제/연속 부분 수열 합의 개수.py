def solution(elements):
    answer = set()
    length = len(elements)
    elements += elements
    for i in range(1, length+1):
        for j in range(length):
            answer.add(sum(elements[j:j+i]))
    return len(answer)

if __name__ == '__main__':
    print(solution([7,9,1,1,4]))