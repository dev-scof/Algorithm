def solution(elements):
    answer = set()
    n = len(elements)
    elements+=elements
    for i in range(n+1):
        for j in range(n+1):
            answer.add(sum(elements[i:i+j]))
    return len(answer)-1

print(solution([7,9,1,1,4]))