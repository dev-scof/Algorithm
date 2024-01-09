N = int(input())
A = list(map(int, input().split()))
answer = -1e9
cur_sum=0
for num in A:
    cur_sum+=num
    if answer<cur_sum:
        answer=cur_sum
    if cur_sum<0:
        cur_sum=0
        continue
print(answer)