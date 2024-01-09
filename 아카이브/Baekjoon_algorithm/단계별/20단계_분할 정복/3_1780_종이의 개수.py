import sys
input = sys.stdin.readline
N = int(input())
answer = [0,0,0]
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().rstrip().split())))

def divide_9(matrix, index, N):
    # print("*"*30)
    f_i, f_j = index[0], index[1]
    # 개수가 1인 경우
    if N==1:
        # print('N=1, matrix[f_i][f_j] = ', matrix[f_i][f_j])
        answer[matrix[f_i][f_j]]+=1
    
    # 1이 아닌 경우
    else:
        
        flag=True
        cur_num=matrix[f_i][f_j]
        # 모두 같은 수인지 체크
        for i in range(f_i, f_i+N):
            if not flag:
                break                
            for j in range(f_j, f_j+N):
                # print(matrix[i][j], end=' ')
                if cur_num != matrix[i][j]:
                    flag = False
                    break
            # print()
        # print('flag = ', flag)
        # 모두 같은 수인 경우
        if flag:
            # print("모두 같은 수")
            # print(cur_num, "삽입")
            answer[cur_num]+=1
        # 복합일 경우
        else:
            # print("복합")
            gap = [0, N//3, N//3*2]
            for i in range(3):
                for j in range(3):
                    divide_9(matrix, [f_i+gap[i], f_j+gap[j]], N//3)

divide_9(matrix, [0,0], N)

print(answer[-1])
print(answer[0])
print(answer[1])

'''
## Log

1. count_num = [0,0,0]을 사용했더니 메모리 초과
-> same_num과 flag를 사용해서 다른 수가 껴있을 경우, flag=False로 하는 로직으로 변경
-> 3%까지 올랐으나, 메모리초과 에러 발생

2. next_index에서 메모리가 초과되지 않았나 추측,
-> s_indexs.pop()을 사용했으나, 메모리 초과 에러 발생

3. next_index.append에서 많은 양의 인덱스가 추가되었을 것으로 추측
-> next_index대신, 바로 함수로 들어가도록 변경
'''