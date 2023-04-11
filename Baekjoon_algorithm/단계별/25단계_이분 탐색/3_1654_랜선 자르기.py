import sys
def bin_cnt(lines, max_len, min_len, N):
    if min_len>max_len:
        return max_len    
    
    mid_len = (max_len+min_len) // 2

    # mid_len에 대해서 cnt계산
    cnt = 0
    for i in lines:
        cnt += i//mid_len
    
    # cnt가 클 경우 -> 범위 : mid_len ~ max_len
    if cnt>=N:
        return bin_cnt(lines, max_len, mid_len+1, N)
    # cnt가 작을 경우 -> 범위 : min_len ~ mid_len
    else:
        return bin_cnt(lines, mid_len-1, min_len, N)


input = sys.stdin.readline
K, N = map(int, input().rstrip().split())
len_lines = []
max_len = 0
for i in range(K):
    value = int(input())
    max_len+=value
    len_lines.append(value)

max_len //= N

print(bin_cnt(len_lines, max_len, 1, N))