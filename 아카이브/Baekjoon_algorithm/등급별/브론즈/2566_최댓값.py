answer1=0
answer2=[0,0]
for i in range(9):
    line = list(map(int, input().split()))
    line_max = max(line)
    if line_max>answer1:
        answer1=line_max
        answer2=[i, line.index(line_max)]
print(answer1)
print(' '.join(map(lambda x:str(x+1), answer2)))