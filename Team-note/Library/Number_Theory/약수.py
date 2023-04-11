answer = []
def 약수(N):
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            answer.append(i)
    return answer
print(약수(24))