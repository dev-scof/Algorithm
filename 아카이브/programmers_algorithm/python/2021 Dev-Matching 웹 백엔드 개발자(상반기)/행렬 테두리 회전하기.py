def solution(rows, columns, queries):
    result = []
    
    # matrix init
    matrix = []
    n=1
    for i in range(rows):
        rows = []
        for j in range(columns):
            rows.append(n)
            n+=1
        matrix.append(rows)
    
    # exception
    if len(queries) == 1:
        x1, y1, x2, y2 = map(lambda x:x-1, queries[0])
        return [matrix[x1][y1]]
    
    # algorithm
    dx = [0, 1, 0, -1] # i
    dy = [1, 0, -1, 0] # j

    # queries 루프
    for pos in queries: # x가 rows에 해당, y가 cols에 해당
        x1, y1, x2, y2 = map(lambda x:x-1, pos)

        # init rotation_min_num
        rotation_min_num = matrix[x1][y1]

        # cur_i : rows, cur_j : cols
        cur_i = x1
        cur_j = y1

        # init direction
        direction = 0
            
        pre_num = next_num = matrix[cur_i][cur_j]

        # 둘레를 도는 루프
        while direction < 4:
            nx = dx[direction] # rows
            ny = dy[direction] # cols
                
            if  (x1 <= cur_i + nx <= x2) and (y1 <= cur_j + ny <= y2):
                
                # compare rotation_min_num
                if rotation_min_num > matrix[cur_i][cur_j]:
                    rotation_min_num = matrix[cur_i][cur_j]

                # change value
                next_num = matrix[cur_i][cur_j]
                matrix[cur_i][cur_j] = pre_num
                pre_num = next_num

                # move next pos
                cur_i += nx
                cur_j += ny
                    
            else:
                direction +=1
            
        matrix[cur_i][cur_j] = pre_num # 마지막 값 넣기
        result.append(rotation_min_num)

    return result


    
print(solution(6, 6, [
                [2,2,5,4],
                [3,3,6,6],
                [5,1,6,3]
            ]))
# print("************************")
# print(solution(3, 3, [
#                 [1,1,2,2],
#                 [1,2,2,3],
#                 [2,1,3,2],
#                 [2,2,3,3]]))
# print(solution(100, 97, [[1,1,100,97]]))
'''
1  2  3  4  5  6
7  8  9  10 11 12
13 14 15 16 17 18
19 20 21 22 23 24
25 26 27 28 29 30
31 32 33 34 35 36

'''