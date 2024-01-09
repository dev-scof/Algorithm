import sys
input = sys.stdin.readline
N = int(input())

def check_palin(string):
    c_l_idx = 0
    c_r_idx = len(string)-1
    flag = True
    while c_l_idx < c_r_idx:
        if string[c_l_idx] == string[c_r_idx]:
            c_l_idx+=1
            c_r_idx-=1
        else:
            flag=False
            break
    return flag

for _ in range(N):
    string = input().rstrip()
    cnt=0
    l_idx=0
    r_idx=len(string)-1
    while l_idx < r_idx:
        if string[l_idx] == string[r_idx]:
            l_idx+=1
            r_idx-=1
        # 다를 경우 -> 안쪽에서 다시 체크
        else:
            l_flag = check_palin(string[l_idx+1:r_idx+1])
            r_flag = check_palin(string[l_idx:r_idx])
            if l_flag or r_flag:
                cnt=1
            else:
                cnt=2
            break
    if cnt == 0:
        print('0')
    elif cnt == 1:
        print('1')
    else:
        print('2')