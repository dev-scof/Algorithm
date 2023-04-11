person=[]
for _ in range(int(input())):
    x, y = map(int, input().split())
    person.append([x, y, 1])
for i in range(len(person)):
    for j in range(len(person)):
        if i==j:
            continue
        if person[i][0] < person[j][0] and person[i][1] < person[j][1]:
            person[i][2]+=1

for per in person:
    print(per[2], end=' ')