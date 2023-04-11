# 삭제할 인덱스
def rm_index(board, n, m):
    index = set()
    for i in range(n-1):
        for j in range(m-1):
            if board[i][j] != 0 and board[i][j]==board[i][j+1]==board[i+1][j]==board[i+1][j+1]:
                index.add((i, j))
                index.add((i, j+1))
                index.add((i+1, j))
                index.add((i+1, j+1))
    return index

def change_zero(indexes, board):
    for i, j in indexes:
        board[i][j]=0

# 어떻게 이동시켜야하나~
# 1. 각 열의 0의 개수를 세서 스왑 -> 논리 오류! // 이전 단계에서 0으로 처리된 것까지 세는 셈
# 2. 0이 시작되는 부분에서 위로 올라가며 0이 아닌 것을 만날때까지 개수를 셈
def move_elem(board, n, m):
    for j in range(m):
        # print('move test*******************')
        i = n-1
        while i>=0 and board[i][j]!=0:
            i-=1
        # 이동할 원소가 없을 경우 => 패스
        if i<=-1:
            continue
        
        # print('현재 가리키는 값 : ', board[i][j], i, j)
        cur_i = i
        while cur_i>=-1:
            for i in range(cur_i-1, -1, -1):
                if board[i][j]!=0:
                    board[cur_i][j]=board[i][j]
                    board[i][j]=0
                    break
            cur_i-=1            

        
        # print('test')
        # for line in board:
        #     print(line)
        
        
                    
def solution(m, n, board):
    answer = 0
    indexes = rm_index(board, m, n)
    graph = []
    for string in board:
        graph.append(list(string))
    board=graph
    
    while indexes:
        answer+=len(indexes)
        change_zero(indexes, board)
        # print('0으로 바뀐 board')
        # for line in board:
        #     print(line)
        move_elem(board, m, n)
        # print('삭제된 board')
        # for line in board:
        #     print(line)
        indexes = rm_index(board, m, n)
        # print('indexes', indexes)
    return answer
# print(solution(6, 6, 
#     ["AAAAAA", 
#     "CCCCCC", 
#     "AAAAAA", 
#     "CCCCCC", 
#     "AAAAAA", 
#     "CCCCCC"]
# ))

        
# print(solution(6, 6, 
#     ["TTTANT", 
#     "RRFACC", 
#     "RRRFCC", 
#     "TRRRAA", 
#     "TTMMMF", 
#     "TMMTTJ"]
# ))

# print(solution(8, 5, 
#                ["HGNHU", 
#                 "CRSHV", 
#                 "UKHVL", 
#                 "MJHQB", 
#                 "GSHOT", 
#                 "MQMJJ", 
#                 "AGJKK", 
#                 "QULKK"]))
# print(solution(6, 5, ["CCZXZ",
#                       "CCZXZ",
#                       "XXZXZ",
#                       "AAZAA",
#                       "AAAAA",
#                       "ZAAXX"]))
print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))

# print( solution(3,2, ["AA", "AA", "AB"])) # 4
# print( solution(4,2, ["CC", "AA", "AA", "CC"]) )  # 8

# print(solution(6,2, ["DD", "CC", "AA", "AA", "CC", "DD"]) )# 12
# print(solution(8,2, ["FF", "AA", "CC", "AA", "AA", "CC", "DD", "FF"]) )# 8
# print(solution(6,2, ["AA", "AA", "CC", "AA", "AA", "DD"])) # 8

# print( solution(2,2,["AA", "AA"]) ) # 4
# print( solution(2,2, ["AA", "AB"]) ) # 0
# print("*"*12)
# print(solution(7, 5, ['XYZAA', 'XYZAA', 'XYZAA', 'XYZTT', 'XYZCC', 'XYZCC', 'XYZKK']))
# print(solution(6, 5, ['XYZAA', 'XYZAA', 'XYZBB', 'XYCCC', 'XYCCC', 'XYZKK']))
# print(solution(6, 5, ['AAAAA', 'AAAAA', 'AAAAA', 'AAAAA', 'AAAAA', 'AAAAA']))