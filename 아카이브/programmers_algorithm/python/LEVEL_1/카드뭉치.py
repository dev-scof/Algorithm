def solution(cards1, cards2, goal):
    i1=i2=0
    for target in goal:
        if i1<len(cards1) and target==cards1[i1]:
            i1+=1
            continue
        elif i2<len(cards2) and target==cards2[i2]:
            i2+=1
            continue
        else:
            return 'No'
    return 'Yes'
        



print(solution(["i", "drink", "water"],	["want", "to"], ["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"],	["want", "to"], ["i", "want", "to", "drink", "water"]))
