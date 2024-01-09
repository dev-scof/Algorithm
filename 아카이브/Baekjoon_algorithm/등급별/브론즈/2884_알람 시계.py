H, M = map(int, input().split())
result = H*60 + M - 45
if result < 0:
    result+=24*60
print(result//60, result%60)