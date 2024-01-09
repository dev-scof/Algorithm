N = int(input())
A = list(map(int, input().split()))
stack = []
answer = [-1]*N
# 9 5 4 8
stack.append(0) # 시작 인덱스

for i in range(N):
    print('i = ', i, 'stack = ', stack)
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)
print(*answer)