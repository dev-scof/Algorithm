h, m = map(int, input().split())
ov_m = int(input())
time = h*60 + m + ov_m
print(time//60%24, time%60)