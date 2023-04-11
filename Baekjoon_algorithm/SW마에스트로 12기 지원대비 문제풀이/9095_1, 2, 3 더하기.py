import sys
input = sys.stdin.readline
def dfs(array, n):
    answer=0
    if n==0:
        return 1
    if n<0:
        return 0
    for i in range(1, 4):
        array.append(i)
        answer += dfs(array, n-i)
        array.pop()
    return answer


T = int(input())
for _ in range(T):
    n = int(input())
    result = 0
    print(dfs([], n))
        