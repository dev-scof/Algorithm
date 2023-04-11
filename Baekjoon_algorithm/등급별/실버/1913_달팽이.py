n = int(input())
m = int(input())
board=[[0]*n for _ in range(n)]

num=1
i = j = n//2
dir=3 # 위
length=1
while num<=n*n:
    # length만큼 이동
    for _ in range(length):
        board[i][j]=num
        if num == m:
            ans = (i+1, j+1)
        num+=1
        if dir==0:
            # 오른쪽
            j+=1
        elif dir==1:
            # 아래
            i+=1
        elif dir==2:
            # 왼쪽
            j-=1
        elif dir==3:
            # 위
            i-=1
    dir = (dir+1)%4
    if dir==1 or dir==3:
        length+=1


for i in range(n):
    print(' '.join(map(str, board[i])))
print(' '.join(map(str, ans)))