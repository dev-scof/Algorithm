N, M = map(int, input().split())
s=set()
for _ in range(N):
    s.add(input())
answer=0
for _ in range(M):
    st = input()
    if st in s:
        answer+=1
print(answer)