N, M = map(int, input().split())
hear=set()
answer = set()
for _ in range(N):
    hear.add(input())
for _ in range(M):
    name = input()
    if name in hear:
        answer.add(name)
print(len(answer))
print('\n'.join(sorted(list(answer))))