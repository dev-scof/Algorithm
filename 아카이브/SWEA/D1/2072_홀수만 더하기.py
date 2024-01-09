T = int(input())
for _ in range(T):
    print(f'#{_} {sum(filter(lambda x:x%2==1, map(int, input().split())))}')