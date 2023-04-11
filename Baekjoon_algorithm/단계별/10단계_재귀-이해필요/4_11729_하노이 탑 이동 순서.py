def hanoi(n, a, b, c): # n, from, use, to // from : 출발지, use : 임시 장소, to : 목적지
    print('n = %d, from : %d, use : %d, to : %d'%(n, a, b, c))
    if n==1:
        move.append([a,c])
    else:
        hanoi(n-1, a, c, b) # a에서 c를 사용해서 b로 이동
        move.append([a,c])
        hanoi(n-1, b, a, c) # b에서 a를 사용해서 c로 이동

# move를 사용하는 이유 : 이동 횟수를 알아내기 위함
# print로 먼저 출력할 경우 출력 조건이 맞지 않음
move=[]
hanoi(int(input()), 1,2,3)
print(len(move))
for i, j in move:
    print(i, j)