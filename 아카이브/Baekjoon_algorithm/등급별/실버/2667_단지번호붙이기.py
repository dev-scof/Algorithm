board = []
n = int(input())
for _ in range(n):
    board.append(list(map(int, (input()))))

def dfs(i, j, visited:set):
    if i<=-1 or i>=n or j<=-1 or j>=n:
        return False
    if board[i][j]==1:
        visited.add((i, j))
        board[i][j]=0
        dfs(i-1, j, visited)
        dfs(i+1, j, visited)
        dfs(i, j-1, visited)
        dfs(i, j+1, visited)
        return True
    return False

answer = []
cnt=0
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            visited=set()
            dfs(i, j, visited)
            answer.append(len(visited))
            cnt+=1

answer.sort()
print(cnt)
for a in answer:
    print(a)
