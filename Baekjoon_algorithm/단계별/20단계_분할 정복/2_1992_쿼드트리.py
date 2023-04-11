import sys
input = sys.stdin.readline
answer = []
def divide_matrix(matrix, s_indexs, N):
    next_indexs = []
    if N==1:
        for f_i, f_j in s_indexs:
            answer.append(str(matrix[f_i][f_j]))
        return

    for f_i, f_j in s_indexs:
        sum = 0
        for i in range(f_i, f_i+N):
            for j in range(f_j, f_j+N):
                sum+=matrix[i][j]
        if sum==0:
            answer.append('0')
        elif sum==N*N:
            answer.append('1')
        else:
            answer.append('(')
            fi_section = [f_i, f_j]
            s_section = [f_i, f_j+N//2]
            t_section = [f_i+N//2, f_j]
            f_section = [f_i+N//2, f_j+N//2]
            
            next_indexs.append(fi_section)
            next_indexs.append(s_section)
            next_indexs.append(t_section)
            next_indexs.append(f_section)

            divide_matrix(matrix, next_indexs, N//2)
            answer.append(')')
            next_indexs = []
    return
N  = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, list(input().rstrip()))))

divide_matrix(matrix, [[0,0]], N)
print(''.join(answer))


'''
8
11110000
11110000
00011100
00011100
11110000
11110000
11110011
11110011


8
00000000
00000000
00001111
00001111
00011111
00111111
00111111
00111111

'''