import sys
input = sys.stdin.readline
colors = [0,0] # index 0 :흰, index 1 : 파

# indexs = [ [f_i, f_j] ]
def divide_matrix(matrix, s_indexs, N):
    next_indexs = []
    if N==1:
        for f_i, f_j in s_indexs:
            colors[matrix[f_i][f_j]]+=1
        return
    for f_i, f_j in s_indexs:
        sum = 0
        for i in range(f_i, f_i+N):
            for j in range(f_j, f_j+N):
                sum+=matrix[i][j]
        # 전체가 0이면 흰종이
        if sum==0:
            colors[0]+=1
        elif sum==N*N:
            colors[1]+=1
        # 둘다 아닐 경우 -> 분할
        else:
            fi_section = [f_i, f_j]
            s_section = [f_i, f_j+N//2]
            t_section = [f_i+N//2, f_j]
            f_section = [f_i+N//2, f_j+N//2]
            
            next_indexs.append(fi_section)
            next_indexs.append(s_section)
            next_indexs.append(t_section)
            next_indexs.append(f_section)
    divide_matrix(matrix, next_indexs, N//2)

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
divide_matrix(matrix, [[0,0]], N)
for c in colors:
    print(c)