for _ in range(int(input())):
    score=0
    add_score=1
    for i in input():
        if i=='O':
            score+=add_score
            add_score+=1
        else:
            add_score=1
    print(score)