from collections import deque
from json import loads
import sys
input = sys.stdin.readline
print = sys.stdout.write
T = int(input())
for _ in range(T):
    p = input().rstrip() # RDD
    n = input() # 4
    arr = deque(loads(input())) # [1,2,3,4]
    r_cnt = 0

    flag=True
    for f in p:
        if f=='R':
            r_cnt+=1
        else:
            if arr:
                if r_cnt%2==1:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                flag=False
                print('error\n')
                break

    if flag:
        if r_cnt%2==1:
            arr.reverse()
        print('[' + ','.join(map(str, arr)) + ']\n')
