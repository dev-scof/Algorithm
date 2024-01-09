# ACM호텔
n = int(input())
for i in range(n):
    H, W, N = map(int, input().split()) # 6 12 
    floor =  H if N%H==0 else N%H
    number = (N//H)%(W+1) if N%H == 0 else (N//H+1)%(W+1)
    print("%d%02d"% (floor, number))

'''
6 12 6 -> 601 인데, 602 나옴 , N//H+1에 논리 오류있다.


'''