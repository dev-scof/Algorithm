n = int(input())
scores=list(map(int, input().split()))
scores_copy=scores.copy()
M=max(scores)
result=0
for i in scores_copy:
    result+=i/M*100
print(result/n)