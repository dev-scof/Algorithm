import sys
input = sys.stdin.readline
N = int(input())
arr = []
stack = []

for _ in range(N):
    arr.append(int(input()))
while arr:
    if stack == []:
        stack.append(arr.pop())
    else:
        last_item = arr.pop()
        if stack[-1] < last_item:
            stack.append(last_item)
print(len(stack))