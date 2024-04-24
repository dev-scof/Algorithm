# 삭제할 인덱스
def rm_index(board, n, m):
    index = set()
    for i in range(n - 1):
        for j in range(m - 1):
            if board[i][j] != 0 and board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1]:
                index.add((i, j))
                index.add((i, j + 1))
                index.add((i + 1, j))
                index.add((i + 1, j + 1))
    return index


def change_zero(indexes, board):
    for i, j in indexes:
        board[i][j] = 0


def move_elem(board, n, m):
    for j in range(m):
        i = n - 1
        while i >= 0 and board[i][j] != 0:
            i -= 1

        # 이동할 원소가 없을 경우 => 패스
        if i <= -1:
            continue

        cur_i = i
        while cur_i >= -1:
            for i in range(cur_i - 1, -1, -1):
                if board[i][j] != 0:
                    board[cur_i][j] = board[i][j]
                    board[i][j] = 0
                    break
            cur_i -= 1


def solution(m, n, board):
    answer = 0
    indexes = rm_index(board, m, n)
    graph = []
    for string in board:
        graph.append(list(string))
    board = graph

    while indexes:
        answer += len(indexes)
        change_zero(indexes, board)
        move_elem(board, m, n)
        indexes = rm_index(board, m, n)
    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
