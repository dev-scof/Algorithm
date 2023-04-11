T = int(input())
for _ in range(T):
    answer = 0
    k = int(input())
    n = int(input())
    l = [x for x in range(1, n+1)] # 0층
    for i in range(k):
        temp = l.copy()
        for j in range(len(l)):
            temp[j] = sum(l[:j+1])
        l=temp.copy()
    print(l[-1])

''' 더욱 효율적인 코드

for _ in range(int(input())):
    k = int(input())
    n = int(input())

    people = [i for i in range(n + 1)]

    for i in range(k):
        for j in range(1, n + 1):
            people[j] = people[j] + people[j - 1]

    print(people[-1])

'''
