def solution(n, k, cmd): # 처음 선택된 인덱스 k
    first_matrix = []
    cur_matrix = []
    cur_index = k
    for i in range(n):
        first_matrix.append([i, 'O'])
        cur_matrix.append([i, 'O'])
    stack = []
    
    for i in cmd:
        c = i[0]
        if cur_index >= len(cur_matrix): # 현재 행렬에서 벗어날경우(삭제할때)
            cur_index = len(cur_matrix)-1
        if cur_index < 0:
            cur_index = 0
        print("cur_index = ", cur_index)
        print("cur_matrix = ", cur_matrix)
        print("현재 선택된 값 = ", cur_matrix[cur_index])
        print("="*30)
        if c == 'C':
            print("C")
            print("저장된 값 = ", cur_matrix[cur_index])
            remove = cur_matrix.pop(cur_index)
            stack.append(remove) # 복구하기 위하여 저장
        if c == 'Z':
            print("Z")
            re = stack.pop()
            print("복구하는 값 = ", re)
            if re[0] < len(cur_matrix)-1: # 안에 넣을경우
                cur_matrix.insert(re[0], re)
                if re[0] < cur_index:
                    cur_index+=1
            else:
                cur_matrix.append(re)
        if c == 'D':
            temp, mov_num = i.split()
            print(temp, mov_num)
            cur_index += int(mov_num)
            print("아래로 이동", mov_num, "현재 인덱스 = ", cur_index)
        if c == 'U':
            temp, mov_num = i.split()
            print(temp, mov_num)
            cur_index -= int(mov_num)
            print("위로 이동", mov_num, "현재 인덱스 = ", cur_index)
    
    answer = ''
    for i in first_matrix:
        if i in cur_matrix:
            answer+='O'
        else:
            answer+='X'
    print(first_matrix)
    print("=======")
    print(cur_matrix)
    print("======")
    print(answer)
    return answer
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))